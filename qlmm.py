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

    parser.add_argument('name', nargs='?', help='Memo or category name')
    parser.add_argument('-n', '--new', nargs=1, choices=['c', 'cat', 'category', 'm', 'mem', 'memo'], help='Add a new category or a new memo')
    parser.add_argument('-e', '--edit', nargs=1, choices=['c', 'cat', 'category', 'm', 'mem', 'memo'], help='Add a category or a memo')
    parser.add_argument('-l', '--list', action='store_true', help='List categories')
    parser.add_argument('-s', '--search', nargs='+', help='Search memo(s)')
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

    return parser


def main(argv):
    parser = args_parsing()
    args = parser.parse_args()

    if len(argv) == 1:
        parser.print_help()
    else:
        from mmanager.fileshandler import FilesHandlers
        from mmanager.dbhandler import DbHandler

        app_paths = {
            'root': APP_PATH,
            'cwd': APP_CWD
        }

        fh = FilesHandlers(app_paths)
        check_config = fh.check_app_datas()

        if not check_config['db']:
            dbpth = f'{APP_PATH}/data/qlmm.db'
            print(f'Un fichier de configuration de qlmm est introuvable... Emplacement attendu:\n{dbpth}')
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), 'qlmm.db')

        if not check_config['config']:
            configpth
            print(f'Un fichier de configuration de qlmm est introuvable... Emplacement attendu:\n{configpth}')
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), 'config.json')

        dbh = DbHandler(f'{APP_PATH}/data/qlmm.db')

    return EXIT_SUCCESS

if __name__ == '__main__':
    sys.exit(main(sys.argv))
