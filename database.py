import psycopg2
from config import POSTGRES_DB, POSTGRES_PASSWORD,POSTGRES_PORT,POSTGRES_HOST,POSTGRES_USER
import pandas as pd

class Database:
    def __init__(self,conn,cursor):
        self.conn = psycopg2.connect(
            dbname=POSTGRES_DB,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            password=POSTGRES_PASSWORD,
            user=POSTGRES_USER
        )
        self.cursor = self.conn.cursor()

    def insert_data(self, df: pd.DataFrame):



