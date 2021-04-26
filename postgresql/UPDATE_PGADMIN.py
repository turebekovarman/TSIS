import psycopg2
def update_rabotniki(rabotniki_id, rabotniki_name):
    """update vendor name based on the vendor id"""
    sql="""UPDATE rabotniki
             SET rabotniki_name=%s
             WHERE rabotniki_id=%s"""
    conn=None
    updated_rows=0
    try:
        conn=psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="1")
        cur=conn.cursor()
        cur.execute(sql,(rabotniki_name,rabotniki_id))
        updated_rows=cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return updated_rows
if __name__=='__main__':
    update_rabotniki(25,"!@#$%^&*(")
    