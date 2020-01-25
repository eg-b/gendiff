import json
import os


def generate_diff(path_to_file1, path_to_file2):
    first_data, second_data = (
        json.load(open(os.path.realpath(path_to_file1))),
        json.load(open(os.path.realpath(path_to_file2)))
        )
    first_set, second_set = set(first_data.items()), set(second_data.items())
    common_data = dict(first_set.intersection(second_set))
    difference = dict(first_set.symmetric_difference(second_set))
    result = '\n'.join('  {}: {}'.format(k, v) for k, v in common_data.items())
    for k, v in difference.items():
        if k not in second_data.keys():
            result += ('\n - ' + '{}: {}'.format(k, v))
        elif k not in first_data.keys():
            result += ('\n + ' + '{}: {}'.format(k, v))
        else:
            result += ('\n - ' + '{}: {}'.format(k, first_data[k]))
            result += ('\n + ' + '{}: {}'.format(k, second_data[k]))
    return '{' + result + '\n}'
