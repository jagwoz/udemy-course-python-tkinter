import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('500x200')
root.resizable(False, False)
root.title('App')


initial_value = tk.IntVar(value=50)
spin_box = tk.Spinbox(
    root,
    from_=0,
    to=100,
    textvariable=initial_value,
    wrap=False
)
spin_box.pack()


def cmd():
    print(spin_box2.get())


initial_str = tk.StringVar(value=50)
spin_box2 = tk.Spinbox(
    root,
    values=(50, 51, 52, 'Juliet is chief'),
    textvariable=initial_str,
    wrap=True,
    command=cmd
)
spin_box2.pack()

root.mainloop()
