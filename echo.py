import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    parser.add_argument('text', help='text to be manipulated')
    args = parser.parse_args()
    if args.upper:
        pass
    elif args.lower:
        pass
    elif args.title:
        pass
    else:
        pass


if __name__ == "__main__":
    main()
