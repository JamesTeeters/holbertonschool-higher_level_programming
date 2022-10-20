#!/usr/bin/python3
"""take state as argument and list all cities"""
import MySQLdb
import sys

if __name__ == '__main__':
    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3])
    cursor = db_connection.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states\
         ON cities.state_id = states.id WHERE states.name\
             LIKE %s ORDER BY cities.id", {sys.arg[4],})
    rows = cursor.fetchall()
    print(', '.join(row[0] for row in rows))
    cursor.close()
    db_connection.close()
