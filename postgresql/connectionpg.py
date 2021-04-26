import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="1")
cur = conn.cursor()
sql="INSERT INTO tablica(width,height) VALUES(%s,%s)"
width=600
height=400
cur.execute(sql,(width,height))
id = cur.fetchone()[0]
conn.commit()
cur.close()
conn.close()