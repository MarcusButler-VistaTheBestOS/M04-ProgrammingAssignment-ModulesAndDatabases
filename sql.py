# Marcus Ed. Butler
# VERSION: 2024-09-17_R0

import sqlite3


# Connect to the database or create if not exist.
conn = sqlite3.connect("books.db")

# Create a cursor object.
c = conn.cursor()


# Delete the table if it exists to avoid redunancy.
c.execute("DROP TABLE IF EXISTS books")

# Create a new table
c.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER)")


with open("books2.csv", 'r') as f_obj:
    raw_data = f_obj.readlines()


# Go through data and insert into SQL table called books.
for line in raw_data[1:]:
    line_split = line.split(',')
    c.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (line_split[0], line_split[1], line_split[2]))



# Print out the title column in alphabetic order.
c.execute("SELECT title FROM books")

rows = c.fetchall()

for row in rows:
    print(row)


conn.commit()
conn.close()
