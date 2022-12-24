from libs.libraries import *


class MyApp(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.container = tk.Frame(self)
        self.container.grid(padx=60, pady=30, sticky='EW')
        self.frames = dict()

        for FrameClass in (MyFrame, MySecFrame):
            frame = FrameClass(self.container, self, padx=60, pady=30)
            frame.grid(row=0, column=0, sticky='NSEW')
            self.frames[FrameClass] = frame

        self.show_frame(MyFrame)

    def show_frame(self, container):
        frame = self.frames[container]
        self.bind('<Return>', frame.print_value)
        frame.tkraise()


class MyFrame(tk.Frame):
    def __init__(self, container: tk.Frame, controller: MyApp, **kwargs):
        super().__init__(container, **kwargs)
        self.controller = controller
        self.value = tk.StringVar()
        self.value_to_display = tk.StringVar(value='Result')

        labels = [tk.Label(self, text='Label:')]
        displays = [tk.Entry(self, width=15, textvariable=self.value, font=('Arial', 15))]
        labels.append(tk.Label(self, text='Label2:'))
        labels.append(tk.Label(self, textvariable=self.value_to_display))
        buttons = [tk.Button(self, text='Button', command=self.print_value),
                   tk.Button(self, text='switch frame', command=lambda: self.controller.show_frame(MySecFrame))]

        labels[0].grid(row=0, column=0, sticky='W', padx=5, pady=5)  # W - west (text align)
        displays[0].grid(row=0, column=1, sticky='EW', padx=5, pady=5)

        labels[1].grid(row=1, column=0, sticky='W', padx=5, pady=5)
        labels[2].grid(row=1, column=1, sticky='EW', padx=5, pady=5)

        buttons[0].grid(column=0, row=2, columnspan=2, sticky='EW', padx=5, pady=5)
        buttons[1].grid(column=0, row=3, columnspan=2, sticky='EW', padx=5, pady=5)

        for child in self.winfo_children():
            child.grid_configure(padx=20)

        labels[0].focus()

    def print_value(self, *args):
        print(args)
        try:
            self.value_to_display.set(f'{(float(self.value.get()) * math.pi):.3f}')
        except ValueError as e:
            self.value_to_display.set(str(e))


class MySecFrame(tk.Frame):
    def __init__(self, container: tk.Frame, controller: MyApp, **kwargs):
        super().__init__(container, **kwargs)
        self.controller = controller
        self.value = tk.StringVar()
        self.value_to_display = tk.StringVar(value='Result')

        labels = [tk.Label(self, text='Label:')]
        displays = [tk.Entry(self, width=15, textvariable=self.value, font=('Arial', 15))]
        labels.append(tk.Label(self, text='Label2:'))
        labels.append(tk.Label(self, textvariable=self.value_to_display))
        buttons = [tk.Button(self, text='Button', command=self.print_value),
                   tk.Button(self, text='switch frame', command=lambda: self.controller.show_frame(MyFrame))]

        labels[0].grid(row=0, column=0, sticky='W', padx=5, pady=5)  # W - west (text align)
        displays[0].grid(row=0, column=1, sticky='EW', padx=5, pady=5)

        labels[1].grid(row=1, column=0, sticky='W', padx=5, pady=5)
        labels[2].grid(row=1, column=1, sticky='EW', padx=5, pady=5)

        buttons[0].grid(column=0, row=2, columnspan=2, sticky='EW', padx=5, pady=5)
        buttons[1].grid(column=0, row=3, columnspan=2, sticky='EW', padx=5, pady=5)

        for child in self.winfo_children():
            child.grid_configure(padx=20)

        labels[0].focus()

    def print_value(self, *args):
        print(args)
        try:
            self.value_to_display.set(f'{(float(self.value.get()) * math.pi):.3f}')
        except ValueError as e:
            self.value_to_display.set(str(e))


root = MyApp('tkinter application')
root.mainloop()
