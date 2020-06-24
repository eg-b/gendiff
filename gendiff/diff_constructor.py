from gendiff.diff_calculator import compare
import os
import json
import yaml


SUPPORTED_FORMATS = '.yml', '.yaml', '.json'


def generate_diff(render, path_to_file1, path_to_file2):
    if render is None:
        return "Wrong output format. Try these: 'jsontxt', 'json', 'plain'"
    file1_format = os.path.splitext(path_to_file1)[1]
    file2_format = os.path.splitext(path_to_file2)[1]
    file1_data = get_file_data(file1_format, path_to_file1)
    file2_data = get_file_data(file2_format, path_to_file2)
    diff = compare(file1_data, file2_data)
    return render(diff)


def get_file_data(file_format, path_to_file):
    if file_format == '.json':
        return json.load(open(os.path.realpath(path_to_file)))
    elif file_format in ['.yml', '.yaml']:
        return yaml.load(open(os.path.realpath(path_to_file)))
    else:
        print("Wrong file format. Try these: '.yaml', '.yml', '.json'")
        raise SystemExit
