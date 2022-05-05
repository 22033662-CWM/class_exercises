from getpass import getpass
from mysql.connector import connect, Error
try:
    with connect(
        host='127.0.0.1',
        user='root',
        password=getpass("Enter root's password: "),
        database='mydb',
    ) as connection:
        print(connection)
except Error as e:
    print(e)


def display_table_5values(db_table):
    show_db_query = "SELECT * FROM db_table LIMIT 5;"
    with connection.cursor() as cursor:
        cursor.execute(show_db_query)
        for row in cursor.fetchall():
            print(row)


def insert_record_to_table(columns: tuple, new_records: tuple, table: str):
    insert_record_to_table_qry = f'''
        INSERT INTO {table}
        {columns}
        VALUES
        ({new_records})
        '''
    with connection.cursor() as cursor:
        cursor.execute(insert_record_to_table_qry)
        connection.commit()
