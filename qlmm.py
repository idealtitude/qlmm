#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import argparse
import errno

__version__ = '0.2'

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

APP_PATH = os.path.dirname(os.path.realpath(__file__))
APP_CWD = os.getcwd()

parser = argparse.ArgumentParser(prog='qlmm', description='LQMM, Quick and Light Memos Manager', epilog='Help and documentation at https://github.com/idealtitude/qlmm')

parser.add_argument('file', nargs=1, help='The yap file to transpile to html')
parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

args = parser.parse_args()


def main(args):
    '''
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), f_in)
    '''

if __name__ == '__main__':
    sys.exit(main(sys.argv))
