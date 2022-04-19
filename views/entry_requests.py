import sqlite3
import json
from models import Entries, Moods, Tags, Entry_Tag

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
        
        # Initialize empty list to hold all entries
        entries = []
        
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        
        # Iterate list of data returned from the database
        for row in dataset: 
            
            # Create an Entries instance from the current row
            entry = Entries(row['id'], row['entry'], row['mood_id'])
            
            db_cursor.execute("""
                SELECT
                    et.entry_id,
                    et.tag_id,
                    t.name name
                FROM Entry_Tag et
                JOIN Tags t
                    ON t.id = et.tag_id
                WHERE et.entry_id = ?
                """, (row['id'], ))
            
            tag_set = db_cursor.fetchall()
            
            tags = []
            
            for tag in tag_set:
                
                result = Tags(tag['tag_id'], tag['name'])
                
                tags.append(result.__dict__)
            
            entry.tags = tags
            
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
            e.mood_id,
            m.mood
        FROM Entries e
        JOIN Moods m
            ON m.id = e.mood_id
        WHERE e.id = ?
        """, ( id, ))
        
        # Initialize an empty list to hold all entry representations
        entry = []
        
        # Load the single result into memory
        data = db_cursor.fetchone()

        entry = Entries(data['id'], data['entry'], data['mood_id'])
        
        mood = Moods(data['id'], data['mood'])
        
        entry.mood = mood.__dict__
        
        return json.dumps(entry.__dict__)
    
def delete_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        DELETE FROM Entries
        WHERE id = ?
        """, (id, ))

def search_entry(keyword):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            e.id,
            e.entry,
            e.mood_id
        FROM Entries e
        WHERE e.entry LIKE ?
        """, ( '%'+ keyword + '%', ))
        
        # Load the single result into memory
        data = db_cursor.fetchone()
        
        # Create an entry intstance from the current row
        entry = Entries(data['id'], data['entry'], data['mood_id'])
        
        return json.dumps(entry.__dict__)

def create_entry(new_entry):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO Entries
            ( entry, mood_id )
        VALUES
            ( ?, ? );
        """, (new_entry['entry'], new_entry['mood_id'], ))
        
        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid
        
        
        
        dataset = db_cursor.fetchall()
    
        for tag_id in new_entry['tags']:
            db_cursor.execute("""
            INSERT INTO Entry_Tag
                ( entry_id, tag_id )
            VALUES
                ( ?, ? );
            """, (id, tag_id, ))

    return json.dumps(new_entry)

def update_entry(id, new_entry):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        UPDATE Entries
            SET
                entry = ?,
                mood_id = ?
        WHERE id = ?
        """, (new_entry['entry'], new_entry['mood_id'], id, ))
        
        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True