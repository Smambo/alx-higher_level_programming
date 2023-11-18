#!/usr/bin/python3
"""
Import modules for script.
"""
import sys
import MySQLdb


def main(args):
    """
    Script that is safe from sql injections.
    """
    if len(args) != 5:
        raise Exception("4 arguments needed!")
    db = MySQLdb.connect(
            host='localhost',
            user=args[1],
            passwd=args[2],
            db=args[3]
            )
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
            (args[4],))
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    main(sys.argv)
