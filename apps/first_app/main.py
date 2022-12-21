from libs.libraries import *

root = tk.Tk()
root.title('tkinter application')
font.nametofont('TkDefaultFont').configure(size=15)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = tk.Frame(root, padx=30, pady=15)
frame.grid()

value = tk.StringVar()
value_to_display = tk.StringVar(value='Result')


def print_value(*args):
    print(args)
    try:
        value_to_display.set(f'{(float(value.get()) * math.pi):.3f}')
    except ValueError as e:
        value_to_display.set(str(e))


labels = [tk.Label(frame, text='Label:')]
displays = [tk.Entry(frame, width=15, textvariable=value, font=('Arial', 15))]
labels.append(tk.Label(frame, text='Label2:'))
labels.append(tk.Label(frame, textvariable=value_to_display))
buttons = [tk.Button(frame, text='Button', command=print_value)]

labels[0].grid(row=0, column=0, sticky='W', padx=5, pady=5)  # W - west (text align)
displays[0].grid(row=0, column=1, sticky='EW', padx=5, pady=5)

labels[1].grid(row=1, column=0, sticky='W', padx=5, pady=5)
labels[2].grid(row=1, column=1, sticky='EW', padx=5, pady=5)

buttons[0].grid(column=0, row=2, columnspan=2, sticky='EW', padx=5, pady=5)

for child in frame.winfo_children():
    child.grid_configure(padx=20)

labels[0].focus()
root.bind('<Return>', print_value)

root.mainloop()
