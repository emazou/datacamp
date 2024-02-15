from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Date
from pandas import DataFrame, read_csv

engine = create_engine("sqlite:///datacamp.sqlite")
df = read_csv('SQL_result.csv')
df.to_sql(con=engine, name='result', if_exists='replace', index=False)
conn = engine.connect()
metadata = MetaData()
result = Table('result', metadata,
               Column('division', String),
               Column('name', String),
               Column('country', String),
               Column('Div', String),
               Column('Date', Date),
               Column('HomeTeam', String),
               Column('AwayTeam', String),
               Column('FTHG', Integer),
               Column('FTAG', Integer),
               Column('FTR', String),
               Column('season', String)
               )

query = result.select()
exe = conn.execute(query)
re = exe.fetchall()
#for r in re:
#    print(r)

update_stmt = result.update().values(season=2010).where(result.columns.season == 2009)
exe = conn.execute(update_stmt)
output = conn.execute(result.select()).fetchall()
#for r in output:
#    print(r)

delete = result.delete().where(result.columns.HomeTeam == 'Barnsley')
exe = conn.execute(delete)
output = conn.execute(result.select()).fetchall()
for r in output:
    print(r)
conn.close()

