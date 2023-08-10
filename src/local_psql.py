import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
database = os.getenv("DATABASE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

conn = psycopg2.connect("dbname=" + str(database) + " user=" + str(username) + " password=" + str(password))
cur = conn.cursor()
def query_sql(query):
    return cur.execute(query)

query_sql("SELECT * FROM channels")
records = cur.fetchall()
