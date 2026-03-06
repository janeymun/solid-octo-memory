import pandas as pd
from sqlalchemy import ( 
    create_engine, 
    inspect, 
    text, 
    select, 
    MetaData, 
    Table
    )


filepath = "/workspaces/solid-octo-memory/Intermediate/Data/903_database.db" 


# read in 903 data
engine_903 = create_engine(f'sqlite+pysqlite:///{filepath}')
connection = engine_903.connect()
inspection = inspect(engine_903)

table_names = inspection.get_table_names()

#uncomment to check database connection and table names
# print(table_names)
# read in the tables as a dictionary of dataframes
metadata_903 = MetaData()

dfs = {}
for table in table_names:
    current_table = Table(table, metadata_903, autoload_with=engine_903)
    with engine_903.connect() as con:
        stmt = select(current_table)
        result = con.execute(stmt).fetchall()
    dfs[table] = pd.DataFrame(result)
#print(dfs.keys()) # check the keys of the dictionary to see the table names
#print(dfs.values())

from Utils import clean_903_table

