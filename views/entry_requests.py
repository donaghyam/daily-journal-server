import sqlite3
import json
from models import Entries

def get_all_entries():
    # Open a connection with the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        
        # black boxes
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        # SQL query to get journal entries
        db_cursor.execute("""
        SELECT
            e.id,
            e.entry,
            e.mood_id
        FROM Entries e
        """)
        
        # Initialize emptry list to hold all entries
        entries = []
        
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        
        # Iterate list of data returned from the database
        for row in dataset: 
            
            # Create an Entries instance from the current row
            entry = Entries(row['id'], row['entry'], row['mood_id'])
            
            # Add the dictionary representation of the entry to the list
            entries.append(entry.__dict__)
            
    # Use json package to properly serialize list as JSON
    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        # Use ? parameter to inject variable's value
        # into the SQL statement
        db_cursor.execute("""
        SELECT
            e.id,
            e.entry,
            e.mood_id
        FROM Entries e
        WHERE e.id = ?
        """, ( id, ))
        
        # Load the single result into memory
        data = db_cursor.fetchone()
        
        # Create an entry intstance from the current row
        entry = Entries(data['id'], data['entry'], data['mood_id'])
        
        return json.dumps(entry.__dict__)
    
def delete_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        DELETE FROM Entries
        WHERE id = ?
        """, (id, ))

        
        
