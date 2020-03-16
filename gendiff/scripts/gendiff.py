#!/usr/bin/env python3
import argparse
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', action='store',
                        dest='format', metavar='FORMAT', default='jsontext',
                        help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == "__main__":
    main()
