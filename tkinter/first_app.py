import tkinter as tk


def log():
    print('button clicked!')


root = tk.Tk()
root.geometry('500x200')

value = tk.StringVar()


label = tk.Label(root, text='Text:')
label.pack(side='left', padx=(0, 10))
entry = tk.Entry(root, textvariable=value, width=20)
entry.pack(side='left')

button = tk.Button(root, text="Button", command=log)
button.pack(side='left', expand=True, fill='x')

quit_button = tk.Button(root, text='quit', command=root.destroy, bg='red', fg='white', padx=20, pady=10)
quit_button.pack(side='bottom', fill='x')

root.mainloop()
