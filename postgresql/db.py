import psycopg2
ok = False
conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="1")
ok = True
if ok :
    print("Connected blabla")