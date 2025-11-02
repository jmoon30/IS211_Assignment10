#!/usr/bin/env python3
import sqlite3

DB_PATH = "pets.db"

PERSON_SQL = """
SELECT id, first_name, last_name, age
FROM person
WHERE id = ?;
"""

PETS_SQL = """
SELECT p.name, p.breed, p.age, p.dead
FROM pet AS p
JOIN person_pet AS pp ON pp.pet_id = p.id
WHERE pp.person_id = ?
ORDER BY p.name;
"""

def format_person(row):
    pid, first, last, age = row
    return f"{first} {last}, {age} years old"

def format_pet(row):
    name, breed, age, dead = row
    status = " (deceased)" if int(dead or 0) == 1 else ""
    return f"owned {name}, a {breed}, that was {age} years old{status}."

def main():
    try:
        conn = sqlite3.connect(DB_PATH)
    except sqlite3.Error as e:
        print(f"Error connecting to {DB_PATH}: {e}")
        return

    with conn:
        cur = conn.cursor()
        while True:
            raw = input("Enter a person ID (-1 to exit): ").strip()
            if raw == "-1":
                print("Goodbye.")
                break
            if not raw.isdigit():
                print("Please enter a valid numeric ID or -1 to exit.\n")
                continue

            pid = int(raw)
            cur.execute(PERSON_SQL, (pid,))
            person = cur.fetchone()
            if not person:
                print(f"No person found with ID {pid}.\n")
                continue

            print(format_person(person))
            cur.execute(PETS_SQL, (pid,))
            pets = cur.fetchall()
            if not pets:
                print("No pets associated.\n")
                continue

            for pet in pets:
                print(format_pet(pet))
            print("")

    conn.close()

if __name__ == "__main__":
    main()
