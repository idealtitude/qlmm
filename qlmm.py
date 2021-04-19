#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import argparse
import errno

__version__ = '0.0.1'

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

APP_PATH = os.path.dirname(os.path.realpath(__file__))
APP_CWD = os.getcwd()

def args_parsing():
    parser = argparse.ArgumentParser(prog='qlmm', description='LQMM, Quick and Light Memos Manager', epilog='Help and documentation at https://github.com/idealtitude/qlmm')

    parser.add_argument('-n', '--new', nargs=1, choices=['c', 'cat', 'category', 'm', 'mem', 'memo'], help='Add a new category or a new memo')
    parser.add_argument('-e', '--edit', nargs=1,  choices=['c', 'cat', 'category', 'm', 'mem', 'memo'], help='Add a category or a memo')
    parser.add_argument('-s', '--search', nargs=1, help='Search memo(s)')
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

    return parser


def main(argv):
    parser = args_parsing()
    args = parser.parse_args()

    if len(argv) == 1:
        parser.print_help()
    else:
        # process args
        pass
    '''
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), f_in)
    '''
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
