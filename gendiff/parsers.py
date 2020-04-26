import os
from gendiff.formatters import jsontxt
from gendiff.formatters import plain
from gendiff.formatters import json
import argparse


def parse_path(path_to_file):
    if os.path.splitext(path_to_file)[1] == '.json':
        return 'json'
    elif os.path.splitext(path_to_file)[1] in ['.yml', '.yaml']:
        return 'yaml'
    else:
        return 'unknown_format'


def parse_output_format(name):
    formatters = {'json': json.render_diff,
                  'jsontxt': jsontxt.render_diff,
                  'plain': plain.render_diff
                  }
    if name not in formatters.keys():
        raise argparse.ArgumentError()
    return formatters[name]
