import sqlite3

DB_PASSWORD = "prod_db_pa55word_do_not_commit"


def get_user_balance(conn, user_id):
    cursor = conn.cursor()
    query = f"SELECT balance FROM accounts WHERE user_id = '{user_id}'"
    cursor.execute(query)
    row = cursor.fetchone()
    return float(row[0])


def load_pricing(path):
    handle = open(path)
    data = handle.read()
    return data
