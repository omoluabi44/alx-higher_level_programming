#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    usrnm = sys.argv[1]
    usrpsw = sys.argv[2]
    dbnm = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usrnm,
        passwd=usrpsw,
        db=dbnm)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    row = cur.fetchall()

    for i in row:
        print(i)

    cur.close()
    db.close()
