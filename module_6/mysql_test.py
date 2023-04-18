#Emily Wojan
#CSD 310
#Module 6 Assignment
#April 18, 2023

"""The purpose of this program is to enable access to the MySQL movies
database."""

#Necessary python imports.
import mysql.connector
from mysql.connector import errorcode

#For congiguring the database.
config = {
	"user": "movies_user",
	"password": "popcorn",
	"host": "127.0.0.1",
	"database": "movies",
	"raise_on_warnings": True
}

#For testing the connection with the MySQL database.
try:
	db = mysql.connector.connect(**config)
	
	print("\n Database user {} connected to MySql on host {} with database {}.".format(config["user"], config["host"], config["database"]))
	
	input("\n\n Press any key to continue...")
	
except:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("		The supplied username or password are invalid.")
	
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("		The specified database does not exist.")
		
	else:
		print(err)
		
finally:
	db.close()
	
