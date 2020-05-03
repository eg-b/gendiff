from gendiff.formats_helper import get_file_format
from gendiff.diff_calculator import compare
import os
import json
import yaml


def generate_diff(render, path_to_file1, path_to_file2):
    file1_format = (get_file_format(path_to_file1))
    file2_format = (get_file_format(path_to_file2))
    file1_data, file2_data = get_file_data(file1_format, path_to_file1), \
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