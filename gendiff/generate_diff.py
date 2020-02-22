from gendiff.parsers import parse_paths
import os
import json
import yaml


def generate_diff(path_to_file1, path_to_file2):
    data_format = parse_paths(path_to_file1, path_to_file2)
    if data_format == 'json':
        file1_data, file2_data = (
            json.load(open(os.path.realpath(path_to_file1))),
            json.load(open(os.path.realpath(path_to_file2)))
        )
    elif data_format == 'yaml':
        file1_data, file2_data = (
            (
                yaml.load(open(os.path.realpath(path_to_file1)),
                          Loader=yaml.SafeLoader)
            ),
            (
                yaml.load(open(os.path.realpath(path_to_file2)),
                          Loader=yaml.SafeLoader)
            )
        )
    diff = compare(file1_data, file2_data)
    result = format_diff(file1_data, file2_data, diff)
    return result


def compare(file1_data, file2_data):
    data1_set, data2_set = set(file1_data.keys()), set(file2_data.keys())
    identical, updated = set(), set()
    for k in data1_set.intersection(data2_set):
        if file1_data[k] == file2_data[k]:
            identical.add(k)
        else:
            updated.add(k)
    removed = data1_set.difference(data2_set)
    added = data2_set.difference(data1_set)
    diff = identical, updated, removed, added
    return diff


def format_diff(file1_data, file2_data, diff):
    identical, updated, removed, added = diff
    result = ''
    for k in identical:
        result += ('\n   {}: {}'.format(k, file2_data[k]))
    for k in updated:
        result += ('\n - ' + '{}: {}'.format(k, file1_data[k]))
        result += ('\n + ' + '{}: {}'.format(k, file2_data[k]))
    for k in removed:
        result += ('\n - ' + '{}: {}'.format(k, file1_data[k]))
    for k in added:
        result += ('\n + ' + '{}: {}'.format(k, file2_data[k]))
    return '{' + result + '\n}'
