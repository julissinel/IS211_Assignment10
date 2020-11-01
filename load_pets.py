import sys
import sqlite3

class PetsDB(object):
    def __init__(self):
        self.conn = sqlite3.connect('pets.db')
        self.cursor = self.conn.cursor()

    def create_schema(self):
        try:
            self.cursor.executescript('''
                DROP TABLE IF EXISTS person;
                DROP TABLE IF EXISTS pet;
                DROP TABLE IF EXISTS person_pet;

                CREATE TABLE person (
                    id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    age INTEGER
                );

                CREATE TABLE pet (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    breed TEXT,
                    age INTEGER,
                    dead INTEGER
                );

                CREATE TABLE person_pet (
                    person_id INTEGER,
                    pet_id INTEGER
                );
                ''')
            self.conn.commit()
            print("pets.db schema created")
        
        except:            
            print("Error creating schema")

    def load_data(self):        
        try:
            self.cursor.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", (
                (1, 'James', 'Smith', 41), (2, 'Diana', 'Greene', 23), (3, 'Sara', 'White', 27),(4, 'William', 'Gibson', 23))
                )
            self.cursor.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", (
                                    (1, 'Rusty', 'Dalmation', 4, 1), (2, 'Bella', 'Alaskan Malamute', 3, 0), (3, 'Max', 'Cocker Spaniel', 1, 0),
                                    (4, 'Rocky', 'Beagle', 7, 0), (5, 'Rufus', 'Cocker Spaniel', 1, 0), (6, 'Spot', 'Bloodhound', 2, 1)
                                    )
                                )

            self.cursor.executemany("INSERT INTO person_pet VALUES(?, ?)", ((1, 1),(1, 2),(2, 3),(2, 4),(3, 5),(4, 6)))
            self.conn.commit()
            print("Loaded")
        
        except:
            print("Error loading into database")


def main():
    pets_db = PetsDB()
    pets_db.create_schema()
    pets_db.load_data()

    sys.exit()


if __name__ == '__main__':
    main()
