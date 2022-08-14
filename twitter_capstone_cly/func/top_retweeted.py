import sqlite3
from pathlib import Path


def top_retweeted(db_path: Path = Path("data.db")):
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT user, id, retweet_count FROM tweets ORDER BY retweet_count DESC LIMIT 10")
        return cursor.fetchall()
