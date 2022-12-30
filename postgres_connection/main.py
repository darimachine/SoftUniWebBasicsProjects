import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="db_demos",
    user="postgres",
    password="1123QwER")

cur = connection.cursor()
cur.execute('SELECT * FROM cities')
connection.commit()
for row in cur.fetchall():
    print(row)


connection.close()
