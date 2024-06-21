#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    current_connection = db_connect.cursor()
    current_connection.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = current_connection.fetchall()
    for row in query_rows:
        print(row)
    current_connection.close()
    db_connect.close()
