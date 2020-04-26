#!/usr/bin/env python3
import argparse
from gendiff.generate_diff import generate_diff
from gendiff.parsers import parse_output_format


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', action='store',
                        dest='format', metavar='FORMAT', default='jsontxt',
                        help='set format of output', type=parse_output_format)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    result = generate_diff(args.format, args.first_file, args.second_file)
    print(result)


if __name__ == "__main__":
    main()
