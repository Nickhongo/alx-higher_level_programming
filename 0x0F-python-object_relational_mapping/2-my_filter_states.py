#!/usr/bin/python3
"""This module contains a script that takes in an argument and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format
             (sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)

        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id"
        .format(state_name)
        cursor.execute(query)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
