#!/usr/bin/python3
"""list all states starting with name given by user"""
import MySQLdb
import sys

if __name__ == '__main__':
    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3])
    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name=%s\
             ORDER BY id ASC", {sys.argv[4]})
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db_connection.close()
