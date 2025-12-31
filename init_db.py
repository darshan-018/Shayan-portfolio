import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.executescript("""
-- Admin table
CREATE TABLE IF NOT EXISTS admin (
  id INTEGER PRIMARY KEY,
  username TEXT,
  password TEXT
);

INSERT OR IGNORE INTO admin VALUES (1, 'admin', 'admin123');

-- Videos table
CREATE TABLE IF NOT EXISTS videos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  category TEXT,
  title TEXT,
  youtube_id TEXT,
  description TEXT
);

-- Contacts table
CREATE TABLE IF NOT EXISTS contacts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  phone TEXT,
  email TEXT,
  category TEXT,
  date TEXT,
  message TEXT
);
""")

# Drop old feedback table if exists
cur.execute("DROP TABLE IF EXISTS feedback;")

# Create new feedback table
cur.execute("""
CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    rating INTEGER DEFAULT 5,
    approved INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

cur.executescript("""
-- Todo table
CREATE TABLE IF NOT EXISTS todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
conn.close()
print("Database and feedback table created successfully!")
