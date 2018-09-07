# q.1 create a database of students

import sqlite3

con = sqlite3.connect('Students.db')
print("Opened database successfully")
con.close()

# q.2 take students name and marks from the user

try:
    con = sqlite3.connect('Students.db')
    
    cursor = con.cursor()
    
    query = 'create table students(Name varchar(10) primary key, \
    Marks int(3))'
    
    cursor.execute(query)
    
    print('Table created successfully!!')
    con.commit()
    
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')

a = []
i=0
while(i<10):
    try:
        name = input("Enter name: ")
        marks = int(input('Enter Marks: '))
        if(marks<0 or marks >100):
            raise ValueError('Invalid marks')
            i=i-1
        else:
            t = name,marks
            a.append(t)
            i=i+1
    except  ValueError as o:
        print(o)



# q.3 append the values in 2 columns


try:
    con = sqlite3.connect('Students.db')
    
    cursor = con.cursor()
    
    query = "insert into students(Name, Marks) \
    values(?,?)"
    
    records = l
    
    cursor.executemany(query, records)
    
    con.commit()
    
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')

# q.4 print the names of all the students who scored more than 80 marks
try:
    con = sqlite3.connect('Students.db')
    
    cursor = con.cursor()
    
    query = 'select * from students where Marks > 80'
    
    cursor.execute(query)
    
    data = cursor.fetchall()

    print("Student who scored greater then 80 are :")
    for row in data:
        print('Name: {}'\
             .format(row[0]))
    
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')
