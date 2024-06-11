import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create a new table
def create_table():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            salary REAL
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert a new record
def insert_record():
    name = entry_name.get()
    email = entry_email.get()
    salary = entry_salary.get()
    
    if name and email and salary:
        try:
            conn = sqlite3.connect('my_database.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO employees (name, email, salary) VALUES (?, ?, ?)
            ''', (name, email, float(salary)))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record inserted successfully!")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e.args[0]}")
    else:
        messagebox.showerror("Error", "All fields are required!")

# Function to fetch all records
def fetch_all_records():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM employees
    ''')
    rows = cursor.fetchall()
    conn.close()
    
    text_area.delete('1.0', tk.END)
    for row in rows:
        text_area.insert(tk.END, f"{row}\n")

# Function to update a record
def update_record():
    id = entry_id.get()
    salary = entry_salary.get()
    
    if id and salary:
        try:
            conn = sqlite3.connect('my_database.db')
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE employees SET salary = ? WHERE id = ?
            ''', (float(salary), int(id)))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record updated successfully!")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e.args[0]}")
    else:
        messagebox.showerror("Error", "ID and Salary fields are required!")

# Function to delete a record
def delete_record():
    id = entry_id.get()
    
    if id:
        try:
            conn = sqlite3.connect('my_database.db')
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM employees WHERE id = ?
            ''', (int(id),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record deleted successfully!")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e.args[0]}")
    else:
        messagebox.showerror("Error", "ID field is required!")

# Create the main window
root = tk.Tk()
root.title("CRUD Application")
root.configure(background='#add8e6')

# Create a frame to center the content
frame = tk.Frame(root, bg='#add8e6')
frame.grid(row=0, column=0, padx=20, pady=20)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Define the font
font_settings = ("Times New Roman", 20, "bold")

# Create input fields and labels inside the frame
tk.Label(frame, text="Name", bg='#add8e6', font=font_settings).grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(frame, font=font_settings)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Email", bg='#add8e6', font=font_settings).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(frame, font=font_settings)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Salary", bg='#add8e6', font=font_settings).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_salary = tk.Entry(frame, font=font_settings)
entry_salary.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="ID", bg='#add8e6', font=font_settings).grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_id = tk.Entry(frame, font=font_settings)
entry_id.grid(row=3, column=1, padx=10, pady=5)

# Create buttons for CRUD operations inside the frame
tk.Button(frame, text="Insert", command=insert_record, bg='#add8e6', font=font_settings).grid(row=4, column=0, padx=10, pady=5)
tk.Button(frame, text="Update", command=update_record, bg='#add8e6', font=font_settings).grid(row=4, column=1, padx=10, pady=5)
tk.Button(frame, text="Delete", command=delete_record, bg='#add8e6', font=font_settings).grid(row=4, column=2, padx=10, pady=5)
tk.Button(frame, text="Show All", command=fetch_all_records, bg='#add8e6', font=font_settings).grid(row=5, column=0, columnspan=3, padx=10, pady=5)

# Create a text area to display records inside the frame
text_area = tk.Text(frame, width=60, height=10, bg='#add8e6', font=font_settings)
text_area.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

# Center the frame in the window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create the table if it doesn't exist
create_table()

# Start the GUI event loop
root.mainloop()
