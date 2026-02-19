import sqlite3
import datetime

DB_NAME = "activities.db"


class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.create_tables()

    def create_tables(self):
        c = self.conn.cursor()

        c.execute("""
        CREATE TABLE IF NOT EXISTS activities(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS time_entries(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            activity_id INTEGER,
            start_time TEXT,
            end_time TEXT,
            seconds INTEGER,
            FOREIGN KEY(activity_id) REFERENCES activities(id)
        )
        """)

        self.conn.commit()

    def get_activity_id(self, name):
        c = self.conn.cursor()
        c.execute("INSERT OR IGNORE INTO activities(name) VALUES(?)", (name,))
        self.conn.commit()

        c.execute("SELECT id FROM activities WHERE name=?", (name,))
        return c.fetchone()[0]

    def add_time_entry(self, name, start, end):
        seconds = int((end - start).total_seconds())
        activity_id = self.get_activity_id(name)

        c = self.conn.cursor()
        c.execute("""
            INSERT INTO time_entries(activity_id, start_time, end_time, seconds)
            VALUES (?, ?, ?, ?)
        """, (activity_id, start.isoformat(), end.isoformat(), seconds))

        self.conn.commit()
