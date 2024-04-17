import sqlite3
from nltk.corpus import wordnet

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
        
    def get_synonyms(self, word):
        synonyms = set()
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name().replace('_', ' '))
        print(synonyms)
        return list(synonyms)

    def search_titles(self, partial_title, use_synonyms=True):
        conn = sqlite3.connect('notes.db')
        c = conn.cursor()

        search_terms = [partial_title]  # Always include the original search term

        # Get synonyms for the search term if use_synonyms is True
        if use_synonyms:
            search_terms += self.get_synonyms(partial_title)

        titles = []
        for term in search_terms:
            # Search titles
            c.execute("SELECT title FROM notes WHERE title LIKE ?", ('%' + term + '%',))
            titles += c.fetchall()

            # Search note contents
            c.execute("SELECT title FROM notes WHERE note_text LIKE ?", ('%' + term + '%',))
            titles += c.fetchall()

        conn.close()
        # Convert the list of titles to a set to remove duplicates, then convert it back to a list
        return list(set(title[0] for title in titles))