import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except Exception as e:
    print(e)

root = tk.Tk()
root.geometry('500x200')
root.resizable(False, False)
root.title('App')


option = tk.StringVar()

combo = ttk.Combobox(root, values=('value1', 'value2', 'value3'), textvariable=option)
# combo['values'] = []
combo.pack()


def choose_handler(event):
    print('your choose is {}, {}'.format(option.get(), combo.current()))


combo.bind('<<ComboboxSelected>>', choose_handler)
root.mainloop()
