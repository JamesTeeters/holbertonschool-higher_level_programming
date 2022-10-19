#!/usr/bin/python3
"""list all states in DB"""
import MySQLdb
import sys

if __name__ == '__main__':
    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    usr=sys.argv[1],
                                    passwrd=sys.argv[2],
                                    dbname=sys.argv[3])
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db_connection.close()
