from tkinter import *
from tkinter.ttk import *
from tkinter import font

root = Tk()

font.nametofont('TkDefaultFont').configure(size=15)
font.nametofont('TkTextFont').configure(size=15)

style = Style()
# style.theme_use(style.theme_names()[4])

myAppWarningFont = font.Font(family='Helvetica', size=20, weight='bold')
# myAppWarningFont = font.nametofont('TkTextFont')  # .copy() <- copy
# print(font.families())

style.configure("MyApp.TLabel", foreground="black", background="white", padding=20, font=('Arial', 20), borderlor='#0F0')
style.map("MyApp.TButton",
          foreground=[('pressed', 'red'), ('active', 'white')],
          background=[('pressed', 'blue'), ('active', 'green')],
          font=[('pressed', ('Arial', 25)), ('active', myAppWarningFont)]
          )

style.theme_use(style.theme_names()[0])
print(style.theme_names())
print(style.layout('TLabel'))

l1 = Label(root, text="Test", style="MyApp.TLabel")
l2 = Label(root, text="Test", style="MyApp.TLabel")
b1 = Button(root, text="Click me!", style="MyApp.TButton")
l1.pack()
l2.pack()
b1.pack()

root.mainloop()