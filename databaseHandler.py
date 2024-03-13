import sqlite3

# This class is responsible for handling the database operations

class DatabaseHandler:
    def __init__(self):
        self.create_database()

    def create_database(self):
        conn = sqlite3.connect('notes.db')  # This will create the database file if it doesn't exist
        c = conn.cursor()
        # Create table
        c.execute('''CREATE TABLE IF NOT EXISTS notes
                    (id INTEGER PRIMARY KEY, title TEXT, note_text TEXT)''')
        conn.commit()
        conn.close()

    def save_note_to_db(self, title, text):
        conn = sqlite3.connect('notes.db')
        c = conn.cursor()
        # Check if the note already exists
        c.execute('SELECT id FROM notes WHERE title = ?', (title,))
        note_id = c.fetchone()
        if note_id:
            # Update existing note
            c.execute('UPDATE notes SET note_text = ? WHERE id = ?', (text, note_id[0]))
        else:
            # Insert new note
            c.execute('INSERT INTO notes (title, note_text) VALUES (?, ?)', (title, text))
        conn.commit()
        conn.close()
        print('Note saved to database.')

    def open_note_from_db(self, title):
        conn = sqlite3.connect('notes.db')
        c = conn.cursor()
        c.execute('SELECT note_text FROM notes WHERE title = ?', (title,))
        note_text = c.fetchone()
        conn.close()
        if note_text:
            return note_text[0]
        else:
            return 'Note not found.'
    def search_titles(self, partial_title):
        conn = sqlite3.connect('notes.db')
        c = conn.cursor()
        # Use LIKE for partial matching
        c.execute("SELECT title FROM notes WHERE title LIKE ?", ('%' + partial_title + '%',))
        titles = c.fetchall()
        conn.close()
        return [title[0] for title in titles]