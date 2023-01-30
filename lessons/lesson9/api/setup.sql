CREATE TABLE
    author (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255)
    );

CREATE TABLE
    book(
        id INTEGER PRIMARY KEY,
        title VARCHAR(255),
        author_id INTEGER,
        FOREIGN KEY(author_id) REFERENCES author(id)
    );

CREATE TABLE
    person(
        id INTEGER PRIMARY KEY,
        name VARCHAR(255),
        age INTEGER,
        favorite_book_id INTEGER,
        FOREIGN KEY (favorite_book_id) REFERENCES book(id)
    );