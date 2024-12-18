import sqlite3

conn = sqlite3.connect('delivery.db')
cursor = conn.cursor()

# Create the "Courier" table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Courier (
    courier_id INTEGER PRIMARY KEY,
    last_name TEXT,
    first_name TEXT,
    middle_name TEXT,
    phone TEXT
)
''')

# Create the "Order" table
cursor.execute('''
CREATE TABLE IF NOT EXISTS OrderTable (
    order_id INTEGER PRIMARY KEY,
    sender TEXT,
    receiver TEXT,
    order_date TEXT,
    delivery_price REAL,
    courier INTEGER,
    FOREIGN KEY (courier) REFERENCES Courier(courier_id)
)
''')

cursor.execute("INSERT INTO Courier (courier_id, last_name, first_name, middle_name, phone) VALUES (1, 'Ivanov', 'Ivan', 'Ivanovich', '+7-900-123-45-67')")

cursor.execute("INSERT INTO OrderTable (order_id, sender, receiver, order_date, delivery_price, courier) VALUES (1, 'Company A', 'John Smith', '2024-10-26', 1500.0, 1)")

cursor.execute("UPDATE Courier SET phone = '+7-999-000-11-22' WHERE courier_id = 1")

# Commit changes and close the connection
conn.commit()
conn.close()
