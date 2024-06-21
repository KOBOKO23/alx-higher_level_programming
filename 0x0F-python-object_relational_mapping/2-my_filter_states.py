#!/usr/bin/python3
"""Lists states based on a provided name"""

import MySQLdb
import sys

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        return

    # Extract command-line arguments
    username, password, database, state_name = sys.argv[1:5]

    try:
        # Connect to MySQL database
        conn = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password,
            db=database, charset="utf8"
        )

        # Create a cursor object
        cur = conn.cursor()

        # SQL query with parameterized query
        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC"
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

