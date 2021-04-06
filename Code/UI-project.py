
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = 'Unemployment.db'

    sql_table= """ CREATE TABLE IF NOT EXISTS Unemployment (
                                        PK integer PRIMARY KEY,
                                        Year integer NOT NULL,
                                        Month integer NOT NULL,
                                        Region text,
                                        County text,
                                        Beneficiaries integer NOT NULL,
                                        Benefit_Amount integer NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_table)

        # create tasks table
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()

conn = create_connection('Unemployment.db')
sql_statement = "select * from unemployment"
import pandas as pd
df = pd.read_sql_query(sql_statement, conn)
from IPython.display import display, HTML
display(df)

def execute_sql_statement(insert_statement, conn):
    cur = conn.cursor()
    cur.execute(sql_statement)

    rows = cur.fetchall()

    return rows
sqlite3
INSERT INTO Unemployment(PK, Year, Month, Region, County, Beneficiaries, Benefit_Amount) VALUES(2020,10,'Capital', 'Albany',7600, 7300000)