import psycopg2
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))

private_connection = SourceFileLoader("private_connection", current_file_path + "/private_connection.py").load_module()


def handle_db_queries(command):
    try:
        connect_str = private_connection.private_config()
        conn = psycopg2.connect(host=connect_str["host"],
                                user=connect_str["user"],
                                dbname=connect_str["dbname"],
                                password=connect_str["password"]
                                )
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(command)
        if "SELECT" in command:
            rows = cursor.fetchall()
            cursor.close()
            return rows
        cursor.close()
    except psycopg2.DatabaseError as exception:
        print(exception)
    finally:
        if conn:
            conn.close()