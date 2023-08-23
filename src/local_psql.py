import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

def connection():
    return psycopg2.connect("dbname=" + str(database) + " user=" + str(username) + " host='localhost'" + " password=" + str(password))

def query_sql_fetchall(query):
    try:
        conn = connection()
        cur = conn.cursor()
        cur.execute(query)
        results = None
        if "SELECT" in query:
                results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except Exception as e:
        raise ConnectionError("PSQL")