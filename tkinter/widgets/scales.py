import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('500x200')
root.resizable(False, False)
root.title('App')


def handle_scale_change(even):
    print(scale.get())


current_value = tk.DoubleVar()

scale = tk.Scale(
    root,
    orient='horizontal',
    from_=0,
    to=100,
    command=handle_scale_change,
    variable=current_value
)

scale.pack(fill='x')


root.mainloop()
