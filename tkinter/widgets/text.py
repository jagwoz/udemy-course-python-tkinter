import tkinter as tk
from PIL import Image, ImageTk

"""
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except Exception as e:
    print(e)
"""

root = tk.Tk()
root.geometry('500x200')
root.resizable(False, False)
root.title('App')

text_places = []

for i in range(2):
    text = tk.Text(root, padx=20, pady=20, height=2, width=15)
    text.config(font=('Arial', 14))
    text.grid(column=i*2, row=0)
    text_places.append(text)

text_places[1].insert("1.0", "Type your name...")
text_places[1]['state'] = 'disabled'  # normal

text_0_scrollbar = tk.Scrollbar(root, orient='vertical', command=text_places[0].yview)
text_0_scrollbar.grid(column=1, row=0, sticky='ns')
text_places[0]['yscrollcommand'] = text_0_scrollbar.set


text_content = text_places[0].get("1.0", "end")
print(text_content)

root.mainloop()
