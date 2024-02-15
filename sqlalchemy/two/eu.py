from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, insert, Boolean, and_
import pandas as pd
# Create a connection to the database
engine = create_engine("sqlite:///datacamp.sqlite")
conn = engine.connect()
metadata = MetaData()

Student = Table('Student', metadata,
              Column('Id', Integer(), primary_key=True),
              Column('Name', String(255), nullable=False),
              Column('Major', String(255), default="Math"),
              Column('Pass', Boolean(), default=True)
              )

metadata.create_all(engine) 
print(' \n**Insert one')
query = insert(Student).values(Id=1, Name='Matthew', Major="English", Pass=True)
result = conn.execute(query)
output = conn.execute(Student.select()).fetchall()
print(output)
print(' \n**Insert many')
query = insert(Student)
values_list = [
    {'Id':'2', 'Name':'Nisha', 'Major':"Science", 'Pass':False},
    {'Id':'3', 'Name':'Natasha', 'Major':"Math", 'Pass':True},
    {'Id':'4', 'Name':'Ben', 'Major':"English", 'Pass':False}
    ]
result = conn.execute(query,values_list)
output = conn.execute(Student.select()).fetchall()
print(output)
print(' \n**Selecting all values from the table by SELECT * FROM Student:')
output = conn.execute("SELECT * FROM Student").fetchall()
print(output)
print(' \n**Selecting all values from the table by SELECT Name, Major FROM Student WHERE Pass = True:')
output = conn.execute("SELECT Name, Major FROM Student WHERE Pass = True")
print(output.fetchall())
print(' \n** Using SQLAlchemy API')
query = Student.select().where(Student.columns.Major == 'English')
output = conn.execute(query)
print(output.fetchall())
print(' \n** Applying AND operator')
query = Student.select().where(and_(Student.columns.Major == 'English', Student.columns.Pass != True))
output = conn.execute(query)
print(output.fetchall())
print(' \n** Pandas')
query = Student.select().where(Student.columns.Major.in_(['English','Math']))
output = conn.execute(query)
results = output.fetchall()

data = pd.DataFrame(results)
data.columns = results[0].keys()
print(data.to_string())