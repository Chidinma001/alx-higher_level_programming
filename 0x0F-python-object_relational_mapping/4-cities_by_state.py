#!/usr/bin/python3
"""A module called 4-cities_by_state"""


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
    query = "SELECT c.id, c.name, s.name \
            FROM cities AS c \
            INNER JOIN states AS s \
            ON c.state_id = s.id \
            ORDER BY c.id;"
    cur.execute(query)
    list(map(print, cur.fetchall()))
    cur.close()
    db.close()
