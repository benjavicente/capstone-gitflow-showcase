CREATE TABLE users (
    username VARCHAR NOT NULL,
    PRIMARY KEY (username)
);

CREATE TABLE hashtags (
    name VARCHAR NOT NULL,
    PRIMARY KEY (name)
);

CREATE TABLE tweets (
    id INTEGER,
    user VARCHAR NOT NULL,
    content VARCHAR,
    date timestamp,
    reply_count INTEGER,
    retweet_count INTEGER,
    like_count INTEGER quote_count INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY(user) REFERENCES user (username)
);

CREATE TABLE tweet_hashtag (
    tweet INTEGER,
    hashtag VARCHAR,
    PRIMARY KEY (tweet, hashtag),
    FOREIGN KEY(tweet) REFERENCES tweet (id),
    FOREIGN KEY(hashtag) REFERENCES hashtag (name)
)