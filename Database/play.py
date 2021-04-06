from IPython.display import display, HTML
import pandas as pd
import sqlite3
from sqlite3 import Error

def create_connection(db_file, delete_db=False):
    import os
    if delete_db and os.path.exists(db_file):
        os.remove(db_file)

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
    except Error as e:
        print(e)

    return conn

conn = create_connection('unemployment.db')
sql_statement = "select * from unemployment;"
df = pd.read_sql_query(sql_statement, conn)
display(df)

conn = create_connection('unemployment.db')
sql_statement = "select * from AGI;"
df = pd.read_sql_query(sql_statement, conn)
display(df)

conn = create_connection('unemployment.db')
sql_statement = "select * from income;"
df = pd.read_sql_query(sql_statement, conn)
display(df)