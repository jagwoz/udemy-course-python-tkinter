import tkinter as tk
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
option2 = tk.StringVar()


def click():
    print(option.get())
    print(option2.get())


check = tk.Checkbutton(root, text="check_button",
                       variable=option, onvalue=1, offvalue=0,
                       command=click)

for i in range(3):
    radio = tk.Radiobutton(root, text=f"option {i}", variable=option2, value="option nr {}".format(i),
                           command=click)
    radio.pack()

check.pack()
# check['state'] = 'disabled'


root.mainloop()
