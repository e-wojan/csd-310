#Emily Wojan
#CSD 310
#Module 7 Assignment
#April 25, 2023

"""The purpose of this program is to enable access to the MySQL movies
database and query the MySQL movie database."""

#Necessary python imports.
import mysql.connector
from mysql.connector import errorcode

#For connecting to the movies database.
config = {
	"user": "movies_user",
	"password": "popcorn",
	"host": "127.0.0.1",
	"database": "movies",
	"raise_on_warnings": True
}

db = mysql.connector.connect(**config)

#Used to create a cursor on the connection.
cursor = db.cursor()

#For displaying the Studio Records.
query = "SELECT * from studio" #Used to store the SELECT statement in the variable query.

cursor.execute(query) #Used to execute the operation stored in the variable query.

result=cursor.fetchall() #Used to retreive all rows from the previously executed statement on the cursor.

print("--DISPLAYING Studio RECORDS--")

for row in result:
    print("Studio ID:",row[0])
   
    print("Studio Name:",row[1])
   
    print(" ")

#For displaying the Genre Records.
query = "SELECT * from genre"

cursor.execute(query)

result=cursor.fetchall()

print("--DISPLAYING Genre RECORDS--")

for row in result:
    print("Genre ID:",row[0])
    
    print("Genre Name:",row[1])
    
    print(" ")
    
#For displaying Short Film Records.
query = "SELECT film_name,film_runtime from film where film_runtime<120 "

cursor.execute(query)

result=cursor.fetchall()

print("--DISPLAYING Short Film RECORDS--")

for row in result:
	
    print("Film Name:",row[0])
    
    print("Runtime:",row[1])
    
    print(" ")
    
#For displaying Director Records.
query = "SELECT film_name,film_director from film order by film_director "

cursor.execute(query)

result=cursor.fetchall()

print("--DISPLAYING Director RECORDS in Order--")

for row in result:
    print("Film Name:",row[0])
    
    print("Director:",row[1])
    
    print(" ")

cursor.close() #Used to close the cursor


db.close() #USed to close the connection.
