import sqlite3


conn = sqlite3.connect("charactersdata.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS characters (name text, age integer, profession text)""")

cursor.execute("""INSERT INTO characters VALUES ('Donald Trump', 72, 'politician')""")

conn.commit()

sql = "SELECT * FROM characters"
cursor.execute(sql)
print(cursor.fetchall())


columns = ['name', 'sex', 'type', 'age', 'profession', 'country']



def create_tables(conn, cur):
    cur.execute('DROP TABLE IF EXISTS characters')

    cur.execute('''
        CREATE TABLE characters (
            name text, 
            sex text, 
            type text, 
            age text, 
            profession text, 
            country text
        )''')
    conn.commit()



def add_character(conn, cur, character_params):


    conn.commit()

def count_strings(cur):
    query = "SELECT COUNT(name) FROM characters"
    cur.execute(query)
    result = cur.fetchone()[0]
    return result


