#!/usr/bin/python3
"""This module contains a script that takes in arguments
and displays all values in the states table"""
import MySQLdb
import sys

def search_states(username, password, database, state_name):
    try:
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)
        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        results = cursor.fetchall()

        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)
    username, password, database, state_name = sys.argv[1:]
    search_states(username, password, database, state_name)
