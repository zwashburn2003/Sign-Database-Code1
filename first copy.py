import sqlite3  # Reading SQL and creating queries
import tkinter as tk  # Create GUI in python
from tkinter import filedialog  # Open File Explorer
from tkinter import messagebox  # Not sure yet
from tkinter import ttk  # Import additional tkinter functions
from Options import Options  # Connect to library file

class operations():
    
    # Open a file dialog and return the selected file path
    def open_file(self):
        
        file_path = filedialog.askopenfilename(title="Open a file", filetypes=[("Database files", "*.db"), ("All files", "*.*")])
        if file_path:
            self.clearList()
            dbfile = file_path
            root.title(file_path)
        return dbfile

    # Reset columns
    def clearList(self):
            
            roads.delete('0', 'end')
            listbox.delete('0', 'end')

    # Populate 2nd column
    def songs(self,event):
        
        cursor.execute("SELECT * FROM invoices")

        rows = cursor.fetchall()
        rows.sort()
        for row in rows:
            listbox.insert(tk.END, row)

    # Insert user input into colummn 1 (for the moment)
    def insert(self):

        selected = combo.get()
        user_input = entry.get()
        entry.delete('0', 'end')
        cursor.execute("INSERT INTO artists (Name) VALUES (?)", (selected,))
        conn.commit()
        self.clearList()
        self.initialPrint()

    # Initially print column 1
    def initialPrint(self):
        cursor.execute("SELECT Name FROM artists ")

        rows = cursor.fetchall()
        rows.sort()
        for row in rows:
            roads.insert(tk.END, row)
        
op = operations()

# Open file/database connection
op.open_file = 'C:/Users/zwash/Downloads/chinook.db'
conn = sqlite3.connect(op.open_file)
cursor = conn.cursor()

# Initialize GUI window
root = tk.Tk()
root.state('zoomed')
root.title("Simple GUI Example")

# Create menubar
menubar = tk.Menu(root, background='black',foreground='black',activebackground='white', activeforeground='black')
file = tk.Menu(menubar, tearoff=0,background='white', foreground='black')
file.add_command(label="New")
menubar.add_cascade(label="File", menu=file)

# Add function to menubar
database = tk.Menu(menubar, tearoff=0,background='blue', foreground='black')
database.add_command(label="Open", command=op.open_file)
menubar.add_cascade(label="Database", menu=database)

# Create frame within window
frame = tk.Frame(root)
frame.pack(side="left",pady=20)

# First column
roads = tk.Listbox(frame, width=50, height=100)
roads.bind('<Double-1>', op.songs)
roads.pack(side=tk.LEFT, fill=tk.BOTH)

# Scrollbar for column 1
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=roads.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
roads.config(yscrollcommand=scrollbar.set)

# Create frame within window
frame1 = tk.Frame(root)
frame1.pack(side="left",pady=20)

# Second column
listbox = tk.Listbox(frame1, width=50, height=100)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Scrollbar for column 2
scrollbar = tk.Scrollbar(frame1, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

# Create frame within window
frame2 = tk.Frame(root)
frame2.pack(side='right', pady=20)

# Create textbox for user entry
entry = tk.Entry(frame2)
entry.pack()

# Create button that triggers insert function
insertbutton = tk.Button(frame2, height=1, width=10, text="Insert", command=lambda: op.insert())
insertbutton.pack()

# Create button that triggers clear function
buttonClear = tk.Button(frame2, height=1, width=10, text="Clear",command=lambda: op.clearList())
buttonClear.pack()

# Create textbox for user input
entry1 = tk.Entry(frame2)
entry1.pack()

# Create dropdown menu using Options.py as values
combo = ttk.Combobox(frame2, values=Options)
combo.bind("<<ComboboxSelected>>", op.insert())
combo.pack(pady=20)


# Initial print for column 1
op.initialPrint()



#sql = "UPDATE artists SET name = 'Zach' WHERE name = '{The Doors}'"
#cursor.execute(sql)



root.config(menu=menubar) # Initialize menubar
root.config(bg='white') # Set background of window
root.mainloop() # Open loop
conn.close() # Close file/database connection