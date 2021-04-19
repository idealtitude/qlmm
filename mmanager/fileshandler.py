#-*- coding: utf-8 -*-

import os


class FilesHandlers:
    def __init__(self, app_paths):
        self.app_paths = app_paths

    def check_app_datas(self):
        db_file = f'{self.app_paths["root"]}/data/qlmm.db'
        config_file = f'{self.app_paths["root"]}/data/config.json'
        result = {'db': False, 'config': False}

        if os.path.isfile(db_file):
            result['db'] = True

        if os.path.isfile(config_file):
            result['config'] = True

        return result

    def get_file_rights(self, file, right):
        if right == 'read' and os.access(file, os.R_OK):
            return True
        else:
            return False

        if right == 'write' and os.access(file, os.W_OK):
            return True
        else:
            return False

        return None

    def construct_path(self, file):
        # Absolute or relative
        tmp_path = file

        if not os.path.isabs(file):
            tmp_path = os.path.realpath(file)

        return tmp_path

    def get_content(self, file, splitl=False):
        if self.get_file_rights('read'):
            ct = None
            fd = open(file, 'r')
            ct = fd.read()
            if splitl:
                ct = ct.splitlines()
            fd.close()
            return ct
        else:
            return False

    def write_content(self, file, content):
        if self.get_file_rights('write'):
            fd = open(file, 'w')
            fd.write(content)
            fd.close()
            return True
        else:
            return False
