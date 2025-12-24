import os
import logging
import mysql.connector
from mysql.connector import Error

from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)

class DataInteractor:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        port_value = os.getenv("DB_PORT", "3306")
        try:
            connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("MYSQL_ROOT_PASSWORD"),
                database=os.getenv("MYSQL_DATABASE"),
                port=int(port_value)
            )
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

    def update_contact(self, id, contact_data):
        query = "UPDATE contacts SET first_name = %s, last_name = %s, phone_number = %s WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (contact_data["first_name"], contact_data["last_name"], contact_data["phone_number"], id))
        self.connection.commit()
        return cursor.rowcount > 0

    def delete_contact(self, id):
        query = "DELETE FROM contacts WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (id,))
        self.connection.commit()
        return cursor.rowcount > 0
    
    def update_contact_person_by_field_selection(self, id, field_name, new_value):
        if field_name not in ["first_name", "last_name", "phone_number"]:
            raise ValueError("Invalid field name")
        query = f"UPDATE contacts SET {field_name} = %s WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (new_value, id))
        self.connection.commit()
        return cursor.rowcount > 0





