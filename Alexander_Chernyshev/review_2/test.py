import sqlite3


conn = sqlite3.connect("charactersdata.db")
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS characters')

cursor.execute('''
    CREATE TABLE characters (
        name text, 
        sex text, 
        type text, 
        age text, 
        profession text, 
        country text
    )''')
conn.commit()

if len(cursor.execute("SELECT * FROM characters").fetchall()) == 0:
    cursor.execute("INSERT INTO characters VALUES ('Donald Trump', 'male', 'human', 'old', 'politician', 'USA')")
    cursor.execute("INSERT INTO characters VALUES ('Vladimir Putin', 'male', 'human', 'old', 'politician', 'Russia')")
    cursor.execute("INSERT INTO characters VALUES ('Angela Merkel', 'female', 'human', 'old', 'politician', 'Germany')")
    cursor.execute("INSERT INTO characters VALUES ('Eminem', 'male', 'human', 'middle aged', 'rapper', 'USA')")
    cursor.execute("INSERT INTO characters VALUES ('Drake', 'male', 'human', 'middle aged', 'rapper', 'Canada')")
    cursor.execute("INSERT INTO characters VALUES ('Billie Eilish', 'female', 'human', 'young', 'singer', 'USA')")
    conn.commit()


cursor.execute("SELECT * FROM characters")
for x in cursor.fetchall():
    print(x)

