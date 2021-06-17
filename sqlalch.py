from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

conn = engine.connect()
students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

address = Table(
   'address', meta, 
   Column('id', Integer, primary_key = True), 
   Column('street', String), 
   Column('student_id', Integer), 
)

meta.create_all(engine)

# new_student = {
#    'name': 'Ivan',
#    'lastname': 'Ivanov'
# }

# ins = students.insert().values(**new_student)

# print(str(ins))

from sqlalchemy import text

conn = engine.connect()

# s = (
#    students
#    .delete()
#    .where(students.c.id>=3)
# )
# # print(s)
# result = conn.execute(s)

# s = students.select()
# result = conn.execute(s).fetchall()
# print(result)

# for student in result:
#    print(student)

# conn.execute(students.insert(), [
#    {'name':'Ravi', 'lastname':'Kapoor'},
#    {'name':'Rajiv', 'lastname' : 'Khanna'},
# ])
s = students.select()
result = conn.execute(s).fetchall()
print(result)

# conn.execute(address.insert(), [
#    {'street':'Zhykov', 'student_id': 1},
#    {'street':'Hmelnickogo', 'student_id': 2},
# ])

from sqlalchemy import select, and_, or_

# j = students.join(address, students.c.id==address.c.student_id)

def compare(students):
   return (students.c.id<3, students.c.id>1)

smt = select([students]).where(or_(*compare(students)))
result = conn.execute(smt).fetchall()
print(result)