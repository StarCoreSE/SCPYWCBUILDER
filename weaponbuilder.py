import tkinter as tk
import os

root = tk.Tk()

text = tk.Text(root)
text.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

scrollbar.config(command=text.yview)  
text.config(yscrollcommand=scrollbar.set)

# Get .cs files and insert text
for f in [f for f in os.listdir('.') if f.endswith('.cs')]:
  with open(f, 'r') as file:
     text.insert('end', file.read())

root.mainloop()