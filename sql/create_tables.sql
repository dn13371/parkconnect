CREATE TABLE users (
    UserId INTEGER PRIMARY KEY AUTOINCREMENT,
    Mail TEXT NOT NULL UNIQUE, 
    UserName TEXT NOT NULL UNIQUE, 
    Password TEXT NOT NULL,
    Activated BOOLEAN DEFAULT FALSE,
    Role TEXT DEFAULT admin,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);