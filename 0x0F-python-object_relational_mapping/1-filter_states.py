#!/usr/bin/python3
"""
Import modules for script.
"""
import sys
import MySQLdb


def main(args):
    """."""
    if len(args) != 4:
        raise Exception("3 arguments needed!")
    db = MySQLdb.connect(
            host='localhost',
            user=args[1],
            passwd=args[2],
            db=args[3]
            )
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name like binary 'N%' ORDER BY id ASC"
            )
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    main(sys.argv)
