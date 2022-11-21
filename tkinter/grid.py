import tkinter as tk


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except Exception as e:
    print(e)



def log():
    print('button clicked!')


root = tk.Tk()
root.geometry('500x200')
root.title('App')

value = tk.StringVar()

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
main = tk.Frame(root)
main.grid(column=0, row=0)
text_frame = tk.Frame(root)
text_frame.grid(column=1, row=0)

label = tk.Label(main, text='Text:')
label.grid(padx=(0, 10))
entry = tk.Entry(main, textvariable=value, width=20)
entry.grid(row=1, column=0)
entry.focus()

label = tk.Label(text_frame, text='Text:')
label.grid(padx=(0, 10))
entry = tk.Entry(text_frame, textvariable=value, width=30)
entry.grid()

button = tk.Button(main, text="Button", command=log)
button.grid(row=1, column=1)

quit_button = tk.Button(root, text='quit', command=root.destroy, bg='red', fg='white', padx=20, pady=10)
quit_button.grid(sticky='EW')

root.mainloop()
