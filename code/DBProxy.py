import sqlite3

class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
                                   CREATE TABLE IF NOT EXISTS highscores(
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   name TEXT NOT NULL,
                                   score INTEGER NOT NULL,
                                   date TEXT NOT NULL)
                                '''
                                )

    def save(self, score_dict: dict):
        self.connection.execute('INSERT INTO highscores (name, score, date) VALUES (:name, :score, :date)', score_dict)
        self.connection.commit()

    def ranking(self) -> list:
        return self.connection.execute('SELECT * FROM highscores ORDER BY score DESC LIMIT 7').fetchall()

    def close(self):
        return self.connection.close()