import sqlite3  # Reading SQL and creating queries
import tkinter as tk  # Create GUI in python
from tkinter import filedialog  # Open File Explorer
from tkinter import messagebox

class operations():
    

    def open_file(self):
        # Open a file dialog and return the selected file path
        file_path = filedialog.askopenfilename(title="Open a file", filetypes=[("Database files", "*.db"), ("All files", "*.*")])
        if file_path:
            self.clearList()
            dbfile = file_path
            root.title(file_path)
        return dbfile

    def clearList(self):
        if roads:
            roads.delete('0', 'end')
        if listbox:
            listbox.delete('0', 'end')

    def songs(self,event):
        cursor.execute("SELECT * FROM invoices")

        rows = cursor.fetchall()
        rows.sort()
        for row in rows:
            listbox.insert(tk.END, row)

    def insert(self):
        user_input = entry.get()
        entry.delete('0', 'end')
        cursor.execute("INSERT INTO artists (Name) VALUES (?)", (user_input,))
        conn.commit()
        self.clearList()
        self.initialPrint()
        print(user_input)

    def initialPrint(self):
        cursor.execute("SELECT Name FROM artists ")

        rows = cursor.fetchall()
        rows.sort()
        for row in rows:
            roads.insert(tk.END, row)
        
op = operations()


root = tk.Tk()
root.state('zoomed')

tk.Label(root, text="Insert:")
entry = tk.Entry(root)
entry.pack()

insertbutton = tk.Button(root, height=1, width=10, text="Insert", command=lambda: op.insert())
insertbutton.pack()
root.title("Simple GUI Example")

buttonClear = tk.Button(root, height=1, width=10, text="Clear",command=lambda: op.clearList())
buttonClear.pack()

menubar = tk.Menu(root, background='black',foreground='black',activebackground='white', activeforeground='black')
file = tk.Menu(menubar, tearoff=0,background='white', foreground='black')
file.add_command(label="New")
menubar.add_cascade(label="File", menu=file)

database = tk.Menu(menubar, tearoff=0,background='blue', foreground='black')
database.add_command(label="Open", command=op.open_file)
menubar.add_cascade(label="Database", menu=database)

frame = tk.Frame(root)
frame.pack(side="left",pady=20)

roads = tk.Listbox(frame, width=50, height=100)
roads.bind('<Double-1>', op.songs)
roads.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=roads.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
roads.config(yscrollcommand=scrollbar.set)

frame = tk.Frame(root)
frame.pack(side="left",pady=20)

listbox = tk.Listbox(frame, width=50, height=100)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

op.open_file = 'C:/Users/zwash/Downloads/chinook.db'
conn = sqlite3.connect(op.open_file)
cursor= conn.cursor()

op.initialPrint()



#sql = "UPDATE artists SET name = 'Zach' WHERE name = '{The Doors}'"
#cursor.execute(sql)



root.config(menu=menubar)
root.mainloop()
conn.close()