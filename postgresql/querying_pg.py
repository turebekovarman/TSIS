import psycopg2

def get_rabotniki():
    conn=None
    sql="SELECT * FROM rabotniki"
    try:
        conn=psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="1")
        cur=conn.cursor()
        cur.execute(sql)
        print("The number of parts: ",cur.rowcount)
        row=cur.fetchone()

        while row is not None:
            print(row)
            row=cur.fetchone()
        
        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__=='__main__':
    get_rabotniki()