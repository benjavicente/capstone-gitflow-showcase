import json
from pathlib import Path

from .db import Session, SQLModel, Tweet, User, create_engine


def load_data_to_db(file_path: Path, db_path: Path = Path("data.db")):
    db_path.unlink(missing_ok=True)
    engine = create_engine(db_path.as_posix())
    SQLModel.metadata.create_all(engine)

    # EL archivo de datos se asume que es http://jsonlines.org/
    with file_path.open("r") as file, Session(engine) as session:
        for line in file:
            tweet = json.loads(line)

            tweet_db = Tweet(**tweet)

            if not (user := session.get(User, tweet["user"]["id"])):
                user = User(**tweet["user"])
                session.add(user)

            tweet_db.user_id = user.id
            session.add(tweet_db)
        session.commit()
