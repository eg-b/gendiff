from gendiff.parsers import parse_path
from gendiff.diff_calculator import compare
import os
import json
import yaml


def generate_diff(render, path_to_file1, path_to_file2):
    file1_format = (parse_path(path_to_file1), path_to_file1)
    file2_format = (parse_path(path_to_file2), path_to_file2)
    data = []
    for format in [file1_format, file2_format]:
        if format[0] == 'json':
            data.append(json.load(open(os.path.realpath(format[1]))))
        elif format[0] == 'yaml':
            data.append(yaml.load(open(os.path.realpath(format[1]))))
        else:
            return ("Wrong file format. Try these: .yaml .yml .json")
    file1_data, file2_data = data[0], data[1]
    diff = compare(file1_data, file2_data)
    return render(diff)
