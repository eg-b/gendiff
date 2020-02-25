from gendiff.parsers import parse_paths
import os


def generate_diff(path_to_file1, path_to_file2):
    data_format = parse_paths(path_to_file1, path_to_file2)
    if data_format == 'json':
        import json as data_format
    if data_format == 'yaml':
        import yaml as data_format
    file1_data, file2_data = (
        data_format.load(open(os.path.realpath(path_to_file1))),
        data_format.load(open(os.path.realpath(path_to_file2)))
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
    identical, updated_old, updated_new, removed, added = (
        dict.fromkeys(identical),
        dict.fromkeys(updated),
        dict.fromkeys(updated),
        dict.fromkeys(removed),
        dict.fromkeys(added)
    )
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


def format_diff(diff, indent_lvl=1):
    identical, updated_old, updated_new, removed, added = diff
    diff = identical, updated_new, removed, added
    result = ''
    for group in diff:
        for key in group.keys():
            if type(group[key]) == dict:
                inner_result = ''
                for k, v in group[key].items():
                    inner_result += (
                        '\n' + '    ' * (indent_lvl + 1)
                        + '{}: {}'.format(k, v)
                    )
                value = '{' + inner_result + '\n' + '    ' * (indent_lvl) + '}'
            else:
                value = group[key]
            if key in identical:
                result += (
                    '\n' + '    ' * indent_lvl + '{}: {}'.format(key, value)
                )
            if key in updated_new:
                if (
                    type(updated_old[key]) == dict
                    and type(updated_new[key]) == dict
                ):
                    child = compare(updated_old[key], updated_new[key])
                    value = format_diff(child, indent_lvl + 1)
                    result += (
                        '\n' + '    ' * indent_lvl +
                        '{}: {}'.format(key, value)
                    )
                else:
                    result += (
                        '\n' + '   ' * indent_lvl +
                        '- {}: {}'.format(key, updated_old[key])
                    )
                    result += (
                        '\n' + '   ' * indent_lvl +
                        '+ {}: {}'.format(key, value)
                    )
            if key in removed:
                result += (
                    '\n' + '   ' * indent_lvl +
                    '- {}: {}'.format(key, value)
                )
            if key in added:
                result += (
                    '\n' + '   ' * indent_lvl +
                    '+ {}: {}'.format(key, value)
                )
    return '{' + result + '\n' + '    ' * (indent_lvl - 1) + '}'
