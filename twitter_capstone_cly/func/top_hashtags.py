import sqlite3
from pathlib import Path


def top_hashtags(db_path: Path = Path("data.db")):
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT hashtag, COUNT(*) AS tweets
            FROM tweet_hashtag, hashtags
            WHERE tweet_hashtag.hashtag = hashtags.name
            GROUP BY hashtag
            ORDER BY tweets DESC
            LIMIT 10
        """)
        return cursor.fetchall()
