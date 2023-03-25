#!/usr/bin/python3
"""A module called 1-filter_states"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cur = db.cursor()
    query = "SELECT * FROM `states` WHERE `name` LIKE 'N%';"
    cur.execute(query)
    list(map(print, sorted(cur.fetchall(), key=lambda x: x[0])))
    cur.close()
    db.close()
