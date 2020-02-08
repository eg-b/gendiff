import os, json, yaml


def parse_files(path_to_file1, path_to_file2):
    if str(path_to_file1).endswith('.json') and str(path_to_file2).endswith('.json'):
        file1_data, file2_data = (
            json.load(open(os.path.realpath(path_to_file1))),
            json.load(open(os.path.realpath(path_to_file2)))
            )
    elif str(path_to_file1).endswith('.yaml') and str(path_to_file2).endswith('.yaml'):
        file1_data, file2_data = (
            yaml.load(open(os.path.realpath(path_to_file1)), Loader=yaml.SafeLoader),
            yaml.load(open(os.path.realpath(path_to_file2)), Loader=yaml.SafeLoader)
        )
    return file1_data, file2_data