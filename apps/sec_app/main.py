from libs.libraries import *


class MyApp(tk.Tk):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(title)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky='EW')
        container.columnconfigure(0, weight=1)

        frame = MyFrame(container)
        frame.grid(row=0, column=0, sticky='NSEW')


class MyFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.actual_time = tk.StringVar(value='01:30')
        self.running = True

        frame = ttk.Frame(self, height=100)
        frame.grid(padx=10, pady=0, sticky='NSEW')

        frame_counter = ttk.Label(frame, textvariable=self.actual_time)
        frame_counter.grid()

        self.decrement_time()

    def decrement_time(self):
        actual_time = self.actual_time.get()

        if actual_time != '00:00' and self.running:
            minutes, seconds = actual_time.split(':')
            if int(seconds) > 0:
                seconds = int(seconds) - 1
                minutes = int(minutes)
            else:
                seconds = 59
                minutes = int(minutes) - 1
            self.actual_time.set(f'{minutes:02d}:{seconds:02d}')

        self.after(1000, self.decrement_time)


root = MyApp('tkinter application')
root.mainloop()
