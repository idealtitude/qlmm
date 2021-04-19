#-*- coding: utf-8 -*-

import os
import re
import sqlite3 as sql


class DbHandler:
    def __init__(self, db):
        self.db = db
        self.conn = None

    def db_connect(self):
        self.conn = sql.connect(self.db)

    def db_close(self):
        self.conn.close()

    def db_query(self, query, fetchall=True):
        cur = self.conn.cursor()
        cur.execute(query)
        res = None

        if fetchall:
            res = cur.fetchall()
        else:
            res = cur.fetchone()

        return res

