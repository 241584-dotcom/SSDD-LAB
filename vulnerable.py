import random
import sqlite3

# Vulnerability 1: Hardcoded password
DB_PASSWORD = "super_secret_password_123" 

def get_user(username):
    # Vulnerability 2: SQL Injection (string formatting)
    query = "SELECT * FROM users WHERE username = '%s'" % username
    return query

def generate_token():
    # Vulnerability 3: Weak random number generator
    return random.randint(100000, 999999)

def process_data():
    # Vulnerability 4: Unused variable
    unused_count = 0
    print("Processing...")

process_data()
