import psycopg2

def delete_rabotniki(rabotniki_id):
    conn=None
    rows_deleted=0
    try:
        conn=psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="1")
        cur=conn.cursor()
        cur.execute("DELETE FROM rabotniki WHERE rabotniki_id=%s",(rabotniki_id,))
        rows_deleted=cur.rowcount
        conn.commit()
        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return rows_deleted
if __name__=='__main__':
    deleted_rows=delete_rabotniki(5)
    print('The number of deleted rows: ',deleted_rows)
