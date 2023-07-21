import tkinter as tk
import os
import time

root = tk.Tk()

text = tk.Text(root)
text.pack(fill='both', expand=True)  
text.config(state='disabled')

prev_text = ''

def check_file():

  global prev_text
  
  file_path = 'testconfig.cs'
  
  if os.path.isfile(file_path):
  
    with open(file_path) as f:
      new_text = f.read()

  else:
    print(f"Error: {file_path} not found")
    new_text = ''

  if new_text != prev_text:
    prev_text = new_text
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('1.0', new_text)
    text.config(state='disabled')
    
  root.after(2000, check_file)

check_file()
root.mainloop()