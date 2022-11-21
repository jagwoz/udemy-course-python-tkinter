import tkinter as tk


def log():
    print('button clicked!')


root = tk.Tk()
root.geometry('500x200')
root.title('App')

value = tk.StringVar()

main = tk.Frame(root)
main.pack(side='top', fill='y', expand=True)
text_frame = tk.Frame(root)
text_frame.pack(side='top', fill='y', expand=True)

label = tk.Label(main, text='Text:')
label.pack(side='left', padx=(0, 10))
entry = tk.Entry(main, textvariable=value, width=20)
entry.pack(side='left')
entry.focus()

label = tk.Label(text_frame, text='Text:')
label.pack(side='left', padx=(0, 10))
entry = tk.Entry(text_frame, textvariable=value, width=30)
entry.pack(side='left')

button = tk.Button(main, text="Button", command=log)
button.pack(side='left', expand=True, fill='x')

quit_button = tk.Button(root, text='quit', command=root.destroy, bg='red', fg='white', padx=20, pady=10)
quit_button.pack(side='bottom', fill='x')

root.mainloop()
