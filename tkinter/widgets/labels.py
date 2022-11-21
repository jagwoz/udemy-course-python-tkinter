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

label = tk.Label(root, text='image:', padx=20, pady=20)
label.config(font=('Arial', 20))
label.pack(side='top')

image = Image.open('logo.png').resize((100, 100))
imageTk = ImageTk.PhotoImage(image)
label2 = tk.Label(root, text="click here ->", image=imageTk, padx=10, compound='right')
label2.pack(side='top')

# label2['image'] = ''

root.mainloop()
