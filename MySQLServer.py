#!/usr/bin/env python3
import mysql.connector

# Connect to MySQL server (change user/password/host if needed)
connection = mysql.connector.connect(
    host="localhost",
    user="onychi",        
    password="slyai" 
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
print("Database 'alx_book_store' created successfully!")


if connection and connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection closed.")
