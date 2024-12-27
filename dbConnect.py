import sqlite3

class DBBConnect:
    def __init__(self):
        self._db = sqlite3.connect("resela.db")
        self._db.row_factory = sqlite3.Row
        self._db.execute(
            "CREATE TABLE IF NOT EXISTS Ticket (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Gender TEXT, Comment TEXT)"
        )
        self._db.commit()

    def Add(self, Name, Gender, Comment):
        self._db.execute(
            "INSERT INTO Ticket (Name, Gender, Comment) VALUES (?, ?, ?)", (Name, Gender, Comment)
        )
        self._db.commit()
        return "Request has been submitted successfully."

    def ListRequest(self):
        return self._db.execute("SELECT * FROM Ticket")
