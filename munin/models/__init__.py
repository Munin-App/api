import records

database = records.Database('sqlite:///munin.db')

queries = [
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    created DATETIME DEFAULT CURRENT_TIMESTAMP
)""",
    """
CREATE TABLE IF NOT EXISTS tokens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    token TEXT UNIQUE,
    name TEXT,
    read_only BOOLEAN DEFAULT 1,
    user_id INTEGER,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_used DATETIME
)"""
]

for query in queries:
    database.query(query)

from munin.models.user import User
from munin.models.token import Token
