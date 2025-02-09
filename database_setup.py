import sqlite3

def create_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create Employees table
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS Employees (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Department TEXT NOT NULL,
        Salary INTEGER NOT NULL,
        Hire_Date TEXT NOT NULL
    )''')

    # Create Departments table
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS Departments (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Manager TEXT NOT NULL
    )''')

    # Insert sample data
    employees = [
        ('Alice', 'Sales', 50000, '2021-01-15'),
        ('Bob', 'Engineering', 70000, '2020-06-10'),
        ('Charlie', 'Marketing', 60000, '2022-03-20'),
        ('David', 'Sales', 55000, '2021-04-18'),
        ('Emma', 'Engineering', 75000, '2019-12-01'),
        ('Frank', 'Marketing', 65000, '2022-07-22'),
        ('Grace', 'Sales', 52000, '2022-01-11'),
        ('Harry', 'Engineering', 68000, '2020-09-05'),
        ('Irene', 'Marketing', 62000, '2021-02-25'),
        ('John', 'Sales', 51000, '2021-07-01')
    ]
    departments = [
        ('Sales', 'Alice'),
        ('Engineering', 'Bob'),
        ('Marketing', 'Charlie'),
        ('HR', 'David'),
        ('Finance', 'Emma'),
        ('Operations', 'Frank')
    ]

    # Insert data into Employees and Departments tables
    cursor.executemany('INSERT OR IGNORE INTO Employees (Name, Department, Salary, Hire_Date) VALUES (?, ?, ?, ?)', employees)
    cursor.executemany('INSERT OR IGNORE INTO Departments (Name, Manager) VALUES (?, ?)', departments)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created and data inserted successfully.")
