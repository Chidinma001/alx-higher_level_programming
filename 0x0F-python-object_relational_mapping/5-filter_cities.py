#!/usr/bin/python3
"""A module called 5-filter_cities"""


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
    query = "SELECT * FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name = %s \
            ORDER BY cities.id ASC;"

    cur.execute(query, (argv[4],))
    print(*[ele[2] for ele in cur.fetchall()], sep=", ")
