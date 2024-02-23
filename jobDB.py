
def create_database():
    # Create a connection to the database (will create the database file if not exists)
    conn = sqlite3.connect('jobs.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Create a table to store job data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            location TEXT NOT NULL,
            salary TEXT
        )
    ''')

    # Insert sample job data into the database
    jobs = [
        (1, 'Iron man', 'Bengaluru, India', 'Rs. 10,00,000'),
        (2, 'Dr.Strange', 'Delhi, India', 'Rs. 15,00,000'),
        (3, 'Captain America', 'Remote', None),
        (4, 'Thor', 'San Francisco, USA', '$120,000')
    ]

    cursor.executemany('INSERT INTO jobs VALUES (?, ?, ?, ?)', jobs)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Database created and sample data inserted.")

if __name__ == '__main__':
    create_database()
