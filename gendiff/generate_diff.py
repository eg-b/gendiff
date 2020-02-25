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
    result = format_diff(diff)
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
    identical = dict.fromkeys(identical)
    updated_old = dict.fromkeys(updated)
    updated_new = dict.fromkeys(updated)
    removed = dict.fromkeys(removed)
    added = dict.fromkeys(added)
    for k in identical:
        identical[k] = file1_data[k]
    for k in updated_old:
        updated_old[k] = file1_data[k]
    for k in updated_new:
        updated_new[k] = file2_data[k]
    for k in removed:
        removed[k] = file1_data[k]
    for k in added:
        added[k] = file2_data[k]
    diff = identical, updated_old, updated_new, removed, added
    return diff


def format_diff(diff, depth_level=1):
    identical, updated_old, updated_new, removed, added = diff
    diff = identical, updated_new, removed, added
    result = ''
    for group in diff:
        for key in group.keys():
            if type(group[key]) == dict:
                if key in updated_new:
                    if type(updated_old[key]) == dict and type(updated_new[key]) == dict:
                        child = compare(updated_old[key], updated_new[key])
                        value = format_diff(child, depth_level + 1)
                        result += '\n' + '    ' * depth_level + '{}: {}'.format(key, value)
                else:
                    inner_result = ''
                    for k, v in group[key].items():
                        inner_result += '\n' + '    ' * (depth_level + 1) + '{}: {}'.format(k, v)
                        value = '{' + inner_result + '\n' + '    ' * (depth_level) + '}'
                    result += '\n' + '    ' * depth_level + '{}: {}'.format(key, value)
            else:
                if key in identical:
                    result += '\n' + '    ' * depth_level + '{}: {}'.format(key, group[key])
                elif key in updated_new:
                    result += '\n' + '   ' * depth_level + '- {}: {}'.format(key, updated_old[key])
                    result += '\n' + '   ' * depth_level + '+ {}: {}'.format(key, group[key])
                elif key in removed:
                    result += '\n' + '   ' * depth_level + '- {}: {}'.format(key, group[key])
                elif key in added:
                    result += '\n' + '   ' * depth_level  + '+ {}: {}'.format(key, group[key])
    return '{' + result + '\n' + '    ' * (depth_level - 1) + '}'