import argparse
import sys


def make_upper_case(string):
    return string.upper()


def make_lower_case(string):
    return string.lower()


def make_title_case(string):
    return string.title()


def parse_args(args):
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    parser.add_argument('text', help='text to be manipulated')

    return parser.parse_args(args)


def main():
    parser = parse_args(sys.argv[1:])
    if parser.title:
        print make_title_case(parser.text)
        return
    if parser.lower:
        print make_lower_case(parser.text)
        return
    if parser.upper:
        print make_upper_case(parser.text)
        return
    else:
        print parser.text


if __name__ == "__main__":
    main()
