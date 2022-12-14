#!/usr/bin/python3
"""list all cities starting with the letter N"""
import MySQLdb
import sys

if __name__ == '__main__':
    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3])
    cursor = db_connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
         FROM cities INNER JOIN states ON\
            cities.state_id=states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db_connection.close()
