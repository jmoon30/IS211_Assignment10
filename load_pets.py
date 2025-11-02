#!/usr/bin/env python3
import sqlite3
from contextlib import closing

DB_PATH = "pets.db"

SCHEMA = '''
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS person_pet;
DROP TABLE IF EXISTS pet;
DROP TABLE IF EXISTS person;

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
    pet_id INTEGER,
    FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE,
    FOREIGN KEY(pet_id) REFERENCES pet(id) ON DELETE CASCADE
);
'''

PEOPLE = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23),
]

PETS = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1),
]

PERSON_PET = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6),
]

def main():
    with closing(sqlite3.connect(DB_PATH)) as conn, conn:
        c = conn.cursor()
        c.executescript(SCHEMA)
        c.executemany(
            "INSERT INTO person (id, first_name, last_name, age) VALUES (?, ?, ?, ?);",
            PEOPLE
        )
        c.executemany(
            "INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?);",
            PETS
        )
        c.executemany(
            "INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?);",
            PERSON_PET
        )
        conn.commit()
        print("pets.db created and loaded successfully.")

if __name__ == "__main__":
    main()
