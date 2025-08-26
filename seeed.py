# create the database in sql lite and connecting with it and filling it with fake users
import sqlite3

# Connect (creates db if it doesn’t exist)
conn = sqlite3.connect("employee_status.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS leaves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    leave_type TEXT NOT NULL,
    days_taken INTEGER NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees (id)
)
""")

# Insert fake employees
employees = [
    ("Alice Johnson", "Engineering"),
    ("Bob Smith", "HR"),
    ("Charlie Brown", "Finance"),
    ("Diana Prince", "Engineering"),
    ("Ethan Hunt", "Operations"),
]

cursor.executemany("INSERT INTO employees (name, department) VALUES (?, ?)", employees)

# Insert fake leaves
leaves = [
    (1, "Casual Leave", 3, "2023-09-01", "2023-09-03"),
    (1, "Sick Leave", 2, "2023-07-15", "2023-07-16"),
    (2, "Casual Leave", 1, "2023-08-10", "2023-08-10"),
    (3, "Sick Leave", 5, "2023-06-05", "2023-06-09"),
    (4, "Maternity Leave", 30, "2023-04-01", "2023-04-30"),
    (5, "Casual Leave", 2, "2023-09-12", "2023-09-13"),
]

cursor.executemany("""
INSERT INTO leaves (employee_id, leave_type, days_taken, start_date, end_date)
VALUES (?, ?, ?, ?, ?)
""", leaves)

conn.commit()
conn.close()

print("✅ HR database created with fake data!")
