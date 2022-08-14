import sqlite3
from pathlib import Path


def top_users_by_tweets(db_path: Path = Path("data.db")):
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT user, COUNT(*) AS tweets
            FROM tweets, users
            WHERE tweets.user = users.username
            GROUP BY user
            ORDER BY retweet_count
            DESC LIMIT 10
        """)
        return cursor.fetchall()
