CREATE TABLE IF NOT EXISTS users
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    street TEXT,
    city VARCHAR(20),
    zip VARCHAR(20)
)