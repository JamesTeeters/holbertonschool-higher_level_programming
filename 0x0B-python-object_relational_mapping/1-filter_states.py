#!/usr/bin/python3
"""list all states starting with the letter N"""
import MySQLdb
import sys

if __name__ == '__main__':
    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3])
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE states.name BINARY LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db_connection.close()
