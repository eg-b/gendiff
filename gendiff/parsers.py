
def parse_paths(path_to_file1, path_to_file2):
    if (
            str(path_to_file1).endswith('.json') and
            str(path_to_file2).endswith('.json')
    ):
        data_format = 'json'
    elif (
            str(path_to_file1).endswith('.yaml') and
            str(path_to_file2).endswith('.yaml')
    ):
        data_format = 'yaml'
    return data_format