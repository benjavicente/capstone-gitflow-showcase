
import sqlite3
from pathlib import Path


def top_days(db_path: Path = Path("data.db")):
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT strftime('%Y-%m-%d', date) AS day, COUNT(*) AS tweets
            FROM tweets
            GROUP BY day
            ORDER BY tweets DESC
            LIMIT 10
        """)
        return cursor.fetchall()
