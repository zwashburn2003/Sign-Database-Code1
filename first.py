import sqlite3
import tkinter as tk
# Import SQL for Database read and tkinter for GUI


def insert():
    pass

root = tk.Tk()
root.configure(background='black')

def clearList():
    listbox.delete('0', 'end')

def songs(event):
    cursor.execute("SELECT * FROM invoices")

    rows = cursor.fetchall()

    for row in rows:
        listbox.insert(tk.END, row)

def retrieve():
    inputValue=textBox.get("1.0", "end-1c")
    sql1 = "INSERT INTO artists (Name) VALUES (%s)"
    val1 = inputValue
    cursor.execute(sql1, val1)
    print(inputValue)
textBox =tk.Text(root, height=2, width=10)
textBox.pack()
buttonCommit = tk.Button(root, height=1, width=10, text="Commit",command=lambda: retrieve())
buttonCommit.pack()
root.title("Simple GUI Example")

buttonClear = tk.Button(root, height=1, width=10, text="Clear",command=lambda: clearList())
buttonClear.pack()

menubar = tk.Menu(root, background='black',foreground='black',activebackground='white', activeforeground='black')
file = tk.Menu(menubar, tearoff=0,background='white', foreground='black')
file.add_command(label="New")
menubar.add_cascade(label="File", menu=file)

database = tk.Menu(menubar, tearoff=0,background='blue', foreground='black')
database.add_command(label="Select")
menubar.add_cascade(label="Database", menu=database)

frame = tk.Frame(root)
frame.pack(side="left",pady=20)

roads = tk.Listbox(frame, width=50, height=100)
roads.bind('<Double-1>', songs)
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

dbfile = 'C:/Users/zwash/Downloads/chinook.db'
conn = sqlite3.connect(dbfile)
cursor= conn.cursor()


cursor.execute("SELECT * FROM artists")

rows = cursor.fetchall()

for row in rows:
    roads.insert(tk.END, row)

#sql = "UPDATE artists SET name = 'Zach' WHERE name = '{The Doors}'"
#cursor.execute(sql)


conn.commit()
root.config(menu=menubar)
root.mainloop()
conn.close()