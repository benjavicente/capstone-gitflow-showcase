import json
import re
import sqlite3
from pathlib import Path


def load_data_to_db(file_path: Path, db_path: Path = Path("data.db")):
    HASHTAG_RE = re.compile(r"#([a-zA-Z0-9_]+)")
    db_path.unlink(missing_ok=True)

    # EL archivo de datos se asume que es http://jsonlines.org/
    with file_path.open("r") as file, sqlite3.connect(db_path) as connection:
        # Cargar esquema de la base de datos
        connection.executescript(Path(__file__).parent.joinpath("schema.sql").read_text())

        for line in file:
            tweet = json.loads(line)
            # Insertar el usuario
            user = tweet["user"]
            connection.execute("INSERT OR IGNORE INTO users (username) VALUES (?)", (user["username"],))

            # Insertar los hashtags
            hashtags: set[str] = {match.group(1) for match in  HASHTAG_RE.finditer(tweet["content"])}
            for hashtag in hashtags:
                connection.execute("INSERT OR IGNORE INTO hashtags (name) VALUES (?)" ,(hashtag,))

            # Insertar el tweet
            connection.execute(
                "INSERT INTO tweets (id, user, content, date, retweet_count, like_count) VALUES (?, ?, ?, ?, ?, ?)",
                (tweet["id"], user["username"], tweet["content"], tweet["date"], tweet["retweetCount"], tweet["likeCount"]),
            )

            # Insertar relación tweet-hashtag
            for hashtag in hashtags:
                connection.execute(
                    "INSERT INTO tweet_hashtag (tweet, hashtag) VALUES (?, ?)",
                    (tweet["id"], hashtag),
            )

