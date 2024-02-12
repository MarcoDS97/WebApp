import mysql.connector
from mysql.connector import Error

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'campionato'
}

def create_db_connection():
    return mysql.connector.connect(**db_config)

# Funzione per eseguire query SQL
def execute_query(query, params=None):
    connection = create_db_connection()
    cursor = connection.cursor(dictionary=True)
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def execute_many(query, data):
    connection = create_db_connection()
    cursor = connection.cursor()
    try:
        cursor.executemany(query, data)
        connection.commit()
        print("Query succesful")
    except Error as err:
        print(f"Error: '{err}'")

def execute_query_insert(query, params=None):
    connection = create_db_connection()
    cursor = connection.cursor()

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    connection.commit()

    cursor.close()
    connection.close()
