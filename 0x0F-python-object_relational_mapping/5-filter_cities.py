#!/usr/bin/python3
"""This module contains a script that takes in the name of a state as
an argument and lists all cities of that state,
using the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database
                state_name".format(sys.argv[0]))
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

        cursor.execute("SELECT cities.id, cities.name,
                states.name FROM cities "
                       "JOIN states ON cities.state_id = states.id "
                       "WHERE states.name = %s "
                       "ORDER BY cities.id", (state_name,))

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
