from gendiff.diff_calculator import compare
from gendiff.formatters import FORMATTERS
import os
import json
import yaml


SUPPORTED_FORMATS = '.yml', '.yaml', '.json'


def generate_diff(render, path_to_file1, path_to_file2):
    file1_format, file2_format = get_file_format(path_to_file1),\
                                 get_file_format(path_to_file2)
    file1_data, file2_data = get_file_data(file1_format, path_to_file1),\
                             get_file_data(file2_format, path_to_file1)
    diff = compare(file1_data, file2_data)
    return render(diff)


def get_file_data(file_format, path_to_file):
    if file_format == 'json':
        return json.load(open(os.path.realpath(path_to_file)))
    elif file_format in ['yml', 'yaml']:
        return yaml.load(open(os.path.realpath(path_to_file)))
    else:
        return ("Wrong file format. Try these: .yaml .yml .json")


def get_file_format(path_to_file):
    ext = os.path.splitext(path_to_file)[1]
    if ext in SUPPORTED_FORMATS:
        return ext[1:]
    else:
        return None


def get_output_format(name):
    if name not in FORMATTERS.keys():
        return None
    return FORMATTERS[name]