#!/usr/bin/python3
""" displays all values in the states table of\
 hbtn_0e_0_usa where name matches the argument.
from the database hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    usrnm = sys.argv[1]
    usrpsw = sys.argv[2]
    dbnm = sys.argv[3]
    stnm = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usrnm,
        passwd=usrpsw,
        db=dbnm)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE\
            name = %s ORDER BY id ASC"
    cur.execute(query, (stnm,))

    row = cur.fetchall()

    for i in row:
        print(i)

    cur.close()
    db.close()
