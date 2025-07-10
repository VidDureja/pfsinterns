import tkinter as tk
import sqlite3
from tkinter import messagebox

# Database setup
conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    guest_name TEXT NOT NULL,
    room_number TEXT NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL
)
''')
conn.commit()

# GUI setup
root = tk.Tk()
root.title('Hotel Management System')
root.geometry('600x400')

# Placeholder for GUI components (CRUD operations)
label = tk.Label(root, text='Welcome to the Hotel Management System!', font=('Arial', 16))
label.pack(pady=20)

# TODO: Add forms and buttons for CRUD operations

root.mainloop()

# Close the database connection when the app closes
conn.close() 