import tkinter as tk


class MyApp(tk.Tk):
    def __init__(self, title, w=600, h=400):
        super().__init__()
        self.title(title)
        self.geometry(f'{w}x{h}')

        InputFrame(self).pack()


class InputFrame(tk.Frame):
    def __init__(self, container: MyApp):
        super().__init__(container)

        self.info = tk.StringVar()
        label = tk.Label(self, text='label text')
        label.pack(side='left')
        entry = tk.Entry(self, textvariable=self.info)
        entry.pack(side='left')


root = MyApp('MyApp')
root.mainloop()
