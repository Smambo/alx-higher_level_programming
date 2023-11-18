#!/usr/bin/python3
"""
Import modules for script.
"""
import sys
import MySQLdb


def main(args):
    """
    Script displays all values in database table
    where name matches the argument.
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
            "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC"
            .format(args[4])
            )
    states = cur.fetchall()
    for state in states:
        if state[1] == args[4]:
            print(state)


if __name__ == "__main__":
    main(sys.argv)
