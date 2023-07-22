import tkinter as tk
from tkinter import ttk 
import os
import re

root = tk.Tk()

damage_var = tk.IntVar(value=100)

# Update label when slider changes
def update_label(event):
  damage_label.config(text=damage_var.get())

def save_damage():

  damage = damage_var.get()

  with open('testconfig.cs', 'r') as f:
    contents = f.read()
  
  find = 'BaseDamage = [0-9]*,'
  replace = f'BaseDamage = {damage},'
  new_contents = re.sub(find, replace, contents)

  with open('testconfig.cs', 'w') as f:
     f.write(new_contents)
     
  text.config(state='normal')
  text.delete('1.0', 'end')
  text.insert('1.0', open('testconfig.cs').read())
  text.config(state='disabled')

# Slider updates variable 
slider = ttk.Scale(root, from_=1, to=1000, 
                   variable=damage_var)
slider.pack(fill='x') 

# Bind slider to update label when moved
slider.bind("<Motion>", update_label)

# Label displays slider value  
damage_label = tk.Label(root, text="100")
damage_label.pack()

button = tk.Button(root, text="Save", command=save_damage)
button.pack()

text = tk.Text(root)
text.pack(fill='both', expand=True)
text.insert('1.0', open('testconfig.cs').read())
text.config(state='disabled')

root.mainloop()