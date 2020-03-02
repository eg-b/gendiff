from gendiff.parsers import parse_paths
from gendiff.formatters import jsonlike, plain
from gendiff.diff_calculator import compare
import os


def generate_diff(output_format, path_to_file1, path_to_file2):
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
    if output_format == 'json':
        result = jsonlike.format_diff(diff)
    if output_format == 'plain':
        result = plain.format_diff(diff)
    return result