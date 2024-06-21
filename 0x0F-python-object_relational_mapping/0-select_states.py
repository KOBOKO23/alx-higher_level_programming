#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

def main():
    # Check if the correct number of arguments are provided
    if len(argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        return

    # Extract command-line arguments
    username = argv[1]
    password = argv[2]
    database = argv[3]

    try:
        # Connect to MySQL database
        conn = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password,
            db=database, charset="utf8"
        )

        # Create a cursor object
        cur = conn.cursor()

        # Execute SQL query
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")

        # Fetch all rows
        rows = cur.fetchall()

        # Print each row
        for row in rows:
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

