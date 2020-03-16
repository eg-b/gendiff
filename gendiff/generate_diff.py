from gendiff.parsers import parse_paths
from gendiff.diff_calculator import compare
import os


def generate_diff(path_to_file1, path_to_file2, output_format='jsontext'):
    file_format = parse_paths(path_to_file1, path_to_file2)
    if file_format == 'json':
        import json as file_format
    if file_format == 'yaml':
        import yaml as file_format
    file1_data, file2_data = (
        file_format.load(open(os.path.realpath(path_to_file1))),
        file_format.load(open(os.path.realpath(path_to_file2)))
    )
    diff = compare(file1_data, file2_data)
    if output_format == 'jsontext':
        from gendiff.formatters import jsonlike as output_format
    if output_format == 'plain':
        from gendiff.formatters import plain as output_format
    result = output_format.render_diff(diff)
    return result
