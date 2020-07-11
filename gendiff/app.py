from gendiff.diff import compare
from gendiff import LOADERS
import os


UNKNOWN_FORMAT = 'unknown'
UNKNOWN_OUTPUT_FORMAT_ERROR = "Wrong output format. Try these: " \
                              "'jsontxt', 'json', 'plain'"
UNKNOWN_FILE_FORMAT_ERROR = "Wrong file format. Try these: " \
                            "'.yaml', '.yml', '.json'"


def generate_diff(render, path_to_file1, path_to_file2):
    if render is None:
        return UNKNOWN_OUTPUT_FORMAT_ERROR
    file1_data = get_file_data(path_to_file1)
    file2_data = get_file_data(path_to_file2)
    if file1_data == UNKNOWN_FORMAT or file2_data == UNKNOWN_FORMAT:
        return UNKNOWN_FILE_FORMAT_ERROR
    diff = compare(file1_data, file2_data)
    return render(diff)


def get_file_data(path_to_file):
    _, ext = os.path.splitext(path_to_file)
    loader = LOADERS.get(ext.lower())
    if loader is not None:
        return loader(open(os.path.realpath(path_to_file)))
    return UNKNOWN_FORMAT
