import records

database = records.Database('sqlite:///munin.db')

query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)"""

database.query(query)

from munin.models.user import User
