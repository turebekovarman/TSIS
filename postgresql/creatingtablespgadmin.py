import psycopg2

def tables_1():
    all_tables=(
        '''
        CREATE TABLE rabotniki(
            rabotniki_id INT,
            rabotniki_name VARCHAR(55) 
        )
        ''',
        ''' CREATE TABLE specialnost(
                specialnost_id INT,
                spacialnost_name VARCHAR(55)
        )
        '''
    )
    conn=None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="1")
        cur=conn.cursor()
        for command in all_tables:
            cur.execute(command)
        cur.close()
        conn.commit()#сохранение изменений
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__=='__main__':
    tables_1()

