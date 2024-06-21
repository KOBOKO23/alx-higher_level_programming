#!/usr/bin/python3
"""Lists states based on a provided name"""

import MySQLdb
from sys import argv

def main():
    # Check if the correct number of arguments are provided
    if len(argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        return

    # Extract command-line arguments
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    try:
        # Connect to MySQL database
        conn = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password,
            db=database, charset="utf8"
        )

        # Create a cursor object
        cur = conn.cursor()

        # SQL query with parameterization to avoid SQL injection
        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
        cur.execute(query, (state_name,))

        # Fetch all rows
        query_rows = cur.fetchall()

        # Print each row
        for row in query_rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"MySQLdb error: {e}")

    finally:
        # Close cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    main()

