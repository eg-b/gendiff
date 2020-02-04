import json
import os


def generate_diff(path_to_file1, path_to_file2):
    file1_data, file2_data = (
        json.load(open(os.path.realpath(path_to_file1))),
        json.load(open(os.path.realpath(path_to_file2)))
        )
    intersection, difference = make_compare(file1_data, file2_data)
    result = '\n'.join(
        '   {}: {}'.format(k, v) for k, v in dict(intersection).items()
        )
    for k, v in dict(difference).items():
        if k not in file2_data.keys():
            result += ('\n - ' + '{}: {}'.format(k, v))
        elif k not in file1_data.keys():
            result += ('\n + ' + '{}: {}'.format(k, v))
        else:
            result += ('\n - ' + '{}: {}'.format(k, file1_data[k]))
            result += ('\n + ' + '{}: {}'.format(k, file2_data[k]))
    return '{\n' + result + '\n}'


def make_compare(file1_data, file2_data):
    data1_set, data2_set = set(file1_data.items()), set(file2_data.items())
    intersection = data1_set.intersection(data2_set)
    difference = data1_set.symmetric_difference(data2_set)
    return intersection, difference
