from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, TEXT

# Create a connection to the database
engine = create_engine("sqlite:///european_database.sqlite")

connection = engine.connect()

# Create a metadata object
metadata = MetaData()
# Create  table divisions
division = Table('divisions', metadata, 
                    Column('division', TEXT()), 
                    Column('name', TEXT()),
                    Column('country', TEXT()),
                    schema=None
                )
                
print(repr(metadata.tables['divisions']))
print(division.columns.keys())

query = division.select() #SELECT * FROM divisions
print(query)

exe = connection.execute(query) #executing the query
result = exe.fetchmany(5) #extracting top 5 results
print(result)