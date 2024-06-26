#!/usr/bin/python3
'''Module'''


import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
