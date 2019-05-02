import sqlite3

conn = sqlite3.connect('charactersdata.db')
cursor = conn.cursor()
parameter = 'country'
country = 'USA'
query = 'SELECT * FROM characters'
query_add = ' WHERE ' + parameter + ' = ' + '\'' + country + '\''
for x in cursor.execute(query+query_add).fetchall():
    print(x)
