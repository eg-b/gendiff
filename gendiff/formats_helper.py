import os
from gendiff.formatters import FORMATTERS


SUPPORTED_FORMATS = '.yml', '.yaml', '.json'


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
