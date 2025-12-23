import logging
import mysql.connector
from mysql.connector import Error

logging.basicConfig(level=logging.INFO)


class DataInteractor:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="contacts_db"
            )
            return connection
        except Error as e:
            print(f"Error: {e}")
            logging.info("Failed to connect to the database.")
            return None


    def get_all_contacts(self):
        query = "SELECT * FROM contacts"
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()





