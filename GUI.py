import tkinter as tk

root = tk.Tk()
root.title("Simple GUI Example")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

root.mainloop()