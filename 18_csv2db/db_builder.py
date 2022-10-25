#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

c.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER)")

with open("students.csv", newline='') as csvfile: # open() as __ SAME NAME BELOW
    students_reader = csv.reader(csvfile, delimiter=",") # csv.reader(__, )
    for row in students_reader:
        print(row)
        c.execute("INSERT into students values(name, age, id)")

print("about to print students database")
c.execute("SELECT * FROM students")

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

db.commit() #save changes
db.close()  #close database

# drop tables (CHECK OUT LATER)
# allows you to edit a table existing already/checks if it's there already
