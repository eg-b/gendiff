import argparse
from gendiff.formatters import FORMATTERS


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('-f', '--format', action='store',
                    dest='format', metavar='FORMAT', default='jsontxt',
                    help='set output format: "jsontxt", "plain", "json"',
                    type=FORMATTERS.get)
parser.add_argument('first_file')
parser.add_argument('second_file')
