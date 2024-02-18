#!/usr/bin/python3
"""
This script will take in an argument and display all the values in the states
where `name` matches the argument from the databaes `hbtn_0e_0_usa`.
This time the script will be secure from any SQL injection unlike in no.2!
"""

import MySQLdb as db
from sys import argv

if __name__ = "__main__":
    """
    this line wll ensure that the script runs only if its executed directly
    and not when imported a s a module.
    """
    db_connect = db.connect(user=argv[1], host="localhost", port=3306,
                            passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute( "SELECT * FROM states WHERE  name LIKE \
                       BINARY %(name)s ORDER BY  states.id ASC", {'name': argv[4]})

        rs = db_cursor.fetchall()

        for row in rs:
        print(row)
