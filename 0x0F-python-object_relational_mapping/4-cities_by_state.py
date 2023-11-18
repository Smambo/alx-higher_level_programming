#!/usr/bin/python3
"""
Import modules for script.
"""
import sys
import MySQLdb


def main(args):
    """Script lists all cities from database."""
    if len(args) != 4:
        raise Exception("3 arguments needed!")
    db = MySQLdb.connect(
            host='localhost',
            user=args[1],
            passwd=args[2],
            db=args[3]
            )
    cur = db.cursor()
    cur.execute("SELECT c.id,\
            c.name, s.name FROM cities c\
            JOIN states s ON s.id=c.state_id ORDER BY c.id")
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    main(sys.argv)
