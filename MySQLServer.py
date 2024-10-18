import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

def main():
    try:
        # Replace with your actual connection details
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nkazimulo@Aya"
        )
        cursor = connection.cursor()

        create_database(cursor)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        try:
            cursor.close()
            connection.close()
        except NameError:
            pass

if __name__ == "__main__":
    main()
