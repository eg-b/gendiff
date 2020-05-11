import argparse
from gendiff.generate_diff import get_output_format

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('-f', '--format', action='store',
                    dest='format', metavar='FORMAT', default='jsontxt',
                    help='set format of output', type=get_output_format)
parser.add_argument('first_file')
parser.add_argument('second_file')


