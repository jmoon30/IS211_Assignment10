# IS211 Assignment 10 – Relational Databases (SQL and SQLite)
John Moon <br>
Prof. Ledon <br>
IS 211 - Software App. Programming II <br>
Oct. 28, 2025

## Overview
This assignment demonstrates basic relational database concepts using **SQLite3** in Python.  
It includes two parts:
1. Designing a **music database schema** (`music.sql`)
2. Loading and querying data in an **existing pets database** (`load_pets.py`, `query_pets.py`)

---

## Repository Contents
| File | Description |
|:--|:--|
| `music.sql` | SQL statements that create tables for a music database (Artists, Albums, Songs). |
| `pets.db` | SQLite database file used by the scripts. |
| `load_pets.py` | Python script to insert sample data into `pets.db`. |
| `query_pets.py` | Python script to query people and their pets interactively. |
| `README.md` | Project documentation (this file). |

---

## Part I – Music Database
The **music database** models artists, albums, and songs.

**Tables**
- `artist` – stores artist names and unique IDs.  
- `album` – stores album names and references the artist ID.  
- `song` – stores song titles, album references, track number, and length (in seconds).

Run this schema to build the database:

```bash
sqlite3 music.db < music.sql
```

---

## Part II – Pets Database

### Database Schema
`pets.db` contains three tables:
- `person` (id, first_name, last_name, age)
- `pet` (id, name, breed, age, dead)
- `person_pet` (person_id, pet_id)

`person_pet` acts as a **relationship table**, linking people and their pets (a many-to-many relationship).

---

### Loading Data (`load_pets.py`)
**Purpose:** Insert the provided data records into `pets.db`.

**How to Run:**
```bash
python load_pets.py
```
This creates and populates the database with sample people and pets.

---

### Querying Data (`query_pets.py`)
**Purpose:** Allow a user to look up people and their pets by person ID.

**How to Run:**
```bash
python query_pets.py
```
When prompted:
1. Enter a person ID (1–4) to view their info and pets.  
2. Enter `-1` to exit the program.  

**Example Output:**
```
Enter person ID: 1
James Smith, 41 years old
James Smith owned Rusty, a Dalmatian, that was 4 years old.
James Smith owned Bella, an Alaskan Malamute, that was 3 years old.
```

---

## IDE Instructions (Optional)
If using **VS Code** or **PyCharm**:
1. Open the folder containing this project.
2. Make sure `python` and `sqlite3` are installed and in your PATH.
3. Open a terminal within the IDE and run:
   ```bash
   python load_pets.py
   python query_pets.py
   ```
4. To inspect the database visually, open `pets.db` using the **SQLite Viewer** extension (VS Code).

---

## Requirements Met
✔ Creates relational schema (`music.sql`)  
✔ Loads data into SQLite (`load_pets.py`)  
✔ Queries and displays data (`query_pets.py`)  
✔ User prompt and exit condition implemented  
✔ All scripts and database files organized in GitHub repository `IS211_Assignment10`
