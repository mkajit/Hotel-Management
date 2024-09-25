import tkinter as tk
from tkinter import messagebox
import sqlite3

 # Create a database connection
conn = sqlite3.connect('hotel.db')
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE IF NOT EXISTS customers (
            name text,
            phone text,
            address text,
            checkin text,
            checkout text,
            roomtype text,
            roomno text
            )""")

# Function to insert data into the database
def insert_data(name, phone, address, checkin, checkout, roomtype, roomno):
    c.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?)",
              (name, phone, address, checkin, checkout, roomtype, roomno))
    conn.commit()

# Function to retrieve data from the database
def retrieve_data():
    c.execute("SELECT * FROM customers")
    rows = c.fetchall()
    return rows

# Function to delete data from the database
def delete_data(phone):
    c.execute("DELETE FROM customers WHERE phone=?", (phone,))
    conn.commit()

# GUI
class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")

        # Frames
        self.frame1 = tk.Frame(self.root, bg="gray")
        self.frame1.pack(fill="both", expand=True)

        self.frame2 = tk.Frame(self.root, bg="gray")
        self.frame2.pack(fill="both", expand=True)

        # Labels and Entries
        tk.Label(self.frame1, text="Name", bg="gray").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.frame1, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame1, text="Phone", bg="gray").grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.frame1, width=30)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame1, text="Address", bg="gray").grid(row=2, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.frame1, width=30)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame1, text="Check-in", bg="gray").grid(row=3, column=0, padx=5, pady=5)
        self.checkin_entry = tk.Entry(self.frame1, width=30)
        self.checkin_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.frame1, text="Check-out", bg="gray").grid(row=4, column=0, padx=5, pady=5)
        self.checkout_entry = tk.Entry(self.frame1, width=30)
        self.checkout_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.frame1, text="Room Type", bg="gray").grid(row=5, column=0, padx=5, pady=5)
        self.roomtype_entry = tk.Entry(self.frame1, width=30)
        self.roomtype_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(self.frame1, text="Room No", bg="gray").grid(row=6, column=0, padx=5, pady=5)
        self.roomno_entry = tk.Entry(self.frame1, width=30)
        self.roomno_entry.grid(row=6, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(self.frame2, text="Check-in", command=self.checkin).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self.frame2, text="Check-out", command=self.checkout).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.frame2, text="View Customers", command=self.view_customers).grid(row=0, column=2, padx=5, pady=5)

    def checkin(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        checkin = self.checkin_entry.get()
        checkout = self.checkout_entry.get()
        roomtype = self.roomtype_entry.get()
        roomno = self.roomno_entry.get()

        insert_data(name, phone, address, checkin, checkout, roomtype, roomno)
        messagebox.showinfo("Success", "Customer checked-in successfully")

    def checkout(self):
        phone = 