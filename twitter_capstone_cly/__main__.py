from pathlib import Path

import typer

from .common import load_data_to_db

DEFAULT_JSON_PATH = Path("farmers-protest-tweets-2021-03-5.json")

app = typer.Typer()
top_app = typer.Typer()
app.add_typer(top_app, name="top")

@app.command()
def load(json_path: Path = DEFAULT_JSON_PATH, db_path: Path = Path("data.db")):
    load_data_to_db(json_path, db_path)

@top_app.command()
def users():
    print("users")

@top_app.command()
def tweets():
    print("tweets")

@top_app.command()
def hashtags():
    print("hashtags")

@top_app.command()
def days():
    print("days")


if __name__ == "__main__":
    app()
