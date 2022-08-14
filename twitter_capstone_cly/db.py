from __future__ import annotations

from typing import List, Optional

from sqlmodel import Field, Relationship, Session, SQLModel
from sqlmodel import create_engine as create_engine_sqlmodel


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    description: str
    followers_count: int = Field(alias='followersCount')
    tweets: List[Tweet] = Relationship(back_populates='user')

class HashTagTweet(SQLModel, table=True):
    tweet_id: int = Field(foreign_key="tweet.id", primary_key=True)
    hashtag_name: str = Field(foreign_key="hashtag.name", primary_key=True)

class HashTag(SQLModel, table=True):
    name: str = Field(alias='name', primary_key=True)
    tweets: List[Tweet] = Relationship(back_populates="tweets", link_model=HashTagTweet)

class Tweet(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="tweets")
    hashtags: List[HashTag] = Relationship(back_populates="tweets", link_model=HashTagTweet)
    url: Optional[str] = None
    content: Optional[str] = None
    reply_count: Optional[int] = Field(None, alias='replyCount')
    retweet_count: Optional[int] = Field(None, alias='retweetCount')
    like_count: Optional[int] = Field(None, alias='likeCount')
    quote_count: Optional[int] = Field(None, alias='quoteCount')

def create_engine(db_path: str):
    return create_engine_sqlmodel(f"sqlite:///{db_path}")
