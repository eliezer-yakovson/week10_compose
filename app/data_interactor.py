import os
import logging
import mysql.connector
from mysql.connector import Error

from dotenv import load_dotenv
load_dotenv(".env.local")

logging.basicConfig(level=logging.INFO)

class DataInteractor:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host="db",          # שם השירות מה-docker-compose
                user="root",        # משתמש ברירת המחדל
                password="1234",    # הסיסמה שהוגדרה ב-.env.docker
                database="contacts_db"     # השם שהוגדר ב-.env.docker
                )
                # host=os.getenv("DB_HOST"),
                # user=os.getenv("DB_USER"),
                # password=os.getenv("DB_PASSWORD"),
                # database=os.getenv("DB_NAME"),
                # port=int(os.getenv("DB_PORT"))
            return connection

        except Error as e:
            print(f"Error: {e}")
            logging.info("Failed to connect to the database.")
            return None

            
    def create_contact(self, first_name, last_name, phone_number):
       query = "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)"
       cursor = self.connection.cursor()
       cursor.execute(query, (first_name, last_name, phone_number))
       self.connection.commit()
       return cursor.lastrowid

    def get_all_contacts(self):
        query = "SELECT * FROM contacts"
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()

    def update_contact(self, id, first_name, last_name, phone_number):
        query = "UPDATE contacts SET first_name = %s, last_name = %s, phone_number = %s WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (first_name, last_name, phone_number, id))
        self.connection.commit()
        return cursor.rowcount > 0

    def delete_contact(self, id):
        query = "DELETE FROM contacts WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (id,))
        self.connection.commit()
        return cursor.rowcount > 0





