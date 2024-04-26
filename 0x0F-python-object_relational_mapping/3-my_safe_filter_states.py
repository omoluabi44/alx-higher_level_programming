#!/usr/bin/python3
"""protect against sql injection"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
        )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE %s ", (sys.argv[4],))
    for i in cursor.fetchall():
        print(i)

    cursor.close()
    db.close()
