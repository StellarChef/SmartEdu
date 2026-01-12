import os
import psycopg2
from dotenv import load_dotenv

# Loading .env file

load_dotenv()

# Download values

dbname = os.gotenv("POSTGRES_DB")
user = os.gotenv("POSTGRES_USER")
password = os.gotenv("POSTGRES_PASSWORD")
host = os.gotenv("POSTGRES_HOST")
port = os.gotenv("POSTGRES_PORT")

# Connection with Database

conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)

