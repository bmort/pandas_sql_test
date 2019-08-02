# coding: utf-8
"""Simple test of pandas with mysql.

Create db:
    docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=passwd -d mysql

Requires:
    pandas-sql
"""
import sys
import logging
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base


def get_db():
    """Get a handle to the mysql database."""
    dialect = "mysql"
    driver = "mysqlconnector"
    username = "root"
    password = "passwd"
    host = "localhost"
    port = 3306
    engine = create_engine(
        f"{dialect}+{driver}://{username}:{password}@{host}:{port}/mysql"
    )
    return engine


def drop_table(table_name):
    """Drop the specified table."""
    engine = get_db()
    base = declarative_base()
    metadata = MetaData(engine)
    metadata.reflect()
    table = metadata.tables.get(table_name)
    if table is not None:
        logging.info(f'Deleting {table_name} table')
        base.metadata.drop_all(engine, [table], checkfirst=True)


def write_df(table='my_data'):
    """Write a pandas dataframe to mysql."""
    engine = get_db()
    conn = engine.connect()
    if engine.has_table(table):
        logging.info(f'Table: {table} exists!')
        drop_table(table)
    logging.info(f'Creating  {table} from dataframe.')
    dates = pd.date_range('20190101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)
    df.to_sql(table, con=conn)


def read_df(table='my_data'):
    """Read pandas dataframe from mysql."""
    logging.info(f'Loading dataframe from table: {table}.')
    df = pd.read_sql(table, con=get_db().connect())
    print(df)

if __name__ == '__main__':
    logging.basicConfig(level='INFO', format='%(asctime)s : %(message)s',
                        stream=sys.stdout)
    write_df()
    read_df()
