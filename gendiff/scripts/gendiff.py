#!/usr/bin/env python3
from gendiff.app import generate_diff
from gendiff.cli import parser


def main():
    args = parser.parse_args()
    result = generate_diff(args.format, args.first_file, args.second_file)
    print(result)


if __name__ == "__main__":
    main()
