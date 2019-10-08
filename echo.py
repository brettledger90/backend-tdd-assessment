#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""
import argparse
__author__ = "???"

import sys


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    # parser.add_argument(
    #     '-h', '--help', help='HALP')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    parser.add_argument(
        'text', help='text to be manipulated')

    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    namespace = parser.parse_args(args)
    text = namespace.text
    if namespace.upper:
        text = text.upper()
    if namespace.lower:
        text = text.lower()
    if namespace.title:
        text = text.title()
    return text


if __name__ == '__main__':
    main(sys.argv[1:])
