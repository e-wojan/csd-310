#Emily Wojan
#CSD 310
#Module 8 Assignment
#April 25, 2023

"""The purpose of this program is to enable access to the MySQL movies
database and preform updates and deletions on records within the database."""

#Necessary python imports.
import mysql.connector
from mysql.connector import errorcode

# Method show_films
def show_films(cursor, title):
    #Method used to execute an inner join on all tables.
	cursor.execute('''select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id''')
	films = cursor.fetchall()
	print("\n -- {} --".format(title))

    #For iterating over the film data set and to display the output.
	for film in films:
		 print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(
			film[0], film[1], film[2], film[3]))

# Main method
def main():
	
	#For connecting to the movies database.
	config = {
		"user": "movies_user",
		"password": "popcorn",
		"host": "127.0.0.1",
		"database": "movies",
		"raise_on_warnings": True
}

	db = mysql.connector.connect(**config)
	
	cursor = db.cursor()
	
    #For displaying the existing records in the movies database.
	show_films(cursor, "DISPLAYING FILMS")

    #For inserting a of new film.
	insertQuery = " INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('United 93', '2006', '110', 'Paul Greengrass', (SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'),(SELECT genre_id FROM genre WHERE genre_name = 'Drama') );"
	db.commit()
	cursor.execute(insertQuery)
	show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    #For updating the genre of the film Alien from SciFi to Horror.
	updateQuery = " update film set genre_id = (select genre_id from genre where genre_name = 'Horror') where film_name = 'Alien';"
	db.commit()
	cursor.execute(updateQuery)
	show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    #For deleting the film Gladiator.
	deleteQuery = " delete from film where film_name = 'Gladiator';"
	db.commit()
	cursor.execute(deleteQuery)
	show_films(cursor, "DISPLAYING FILMS AFTER Delete")

main()
