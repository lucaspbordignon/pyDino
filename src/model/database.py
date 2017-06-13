import sqlite3


class database():
    """
            A class tha represents a database. The database engine used is the
            SQLite.
    """
    def __init__(self, db_name='players_database.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        """
            Creates a table inside the database.
        """
        try:
            self.cursor.execute('''CREATE TABLE players
                               (name TEXT PRIMARY KEY, type TEXT, coins INTEGER)
                               ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            return "Table already exists."

    def add(self, values):
        """
            Adds a row with the given values to the table.
        """
        self.cursor.execute('''REPLACE INTO players(name, type, coins)
                            VALUES(:name, :type, :coins)''',
                            values)
        self.connection.commit()

    def close(self):
        """
            Closes the connection with the database.
        """
        self.connection.commit()
        self.connection.close()

    def execute(self, command):
        """
            Executes a given query in the database.
        """
        return self.cursor.execute(command)
