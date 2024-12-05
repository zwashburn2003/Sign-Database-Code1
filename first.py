import sqlite3
import tkinter as tk
# Import SQL for Database read and tkinter for GUI

root = tk.Tk()
root.title("Simple GUI Example")

menubar = tk.Menu(root, background='black',foreground='black',activebackground='white', activeforeground='black')
file = tk.Menu(menubar, tearoff=0,background='white', foreground='black')
file.add_command(label="New")
menubar.add_cascade(label="File", menu=file)

database = tk.Menu(menubar, tearoff=0,background='blue', foreground='black')
database.add_command(label="Select")
menubar.add_cascade(label="Database", menu=database)

frame = tk.Frame(root)
frame.pack(side="left",pady=20)

listbox = tk.Listbox(frame, width=50, height=100)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

frame = tk.Frame(root)
frame.pack(side="left",pady=20)

roads = tk.Listbox(frame, width=50, height=100)
roads.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=roads.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
roads.config(yscrollcommand=scrollbar.set)


label = tk.Label(root, text="Hello, Tkinter!")
label.pack(side="left", pady=10)

dbfile = 'C:/Users/zwash/Downloads/chinook.db'
conn = sqlite3.connect(dbfile)
cursor= conn.cursor()


cursor.execute("SELECT * FROM albums")

rows = cursor.fetchall()

for row in rows:
    listbox.insert(tk.END, row)

root.config(menu=menubar)
root.mainloop()
conn.close()