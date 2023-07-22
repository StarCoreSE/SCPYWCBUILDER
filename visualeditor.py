import tkinter as tk
from tkinter import ttk
import os
import re

# Root window
root = tk.Tk()

# Variables to store values
damage_var = tk.IntVar(value=100)
max_traj_var = tk.IntVar(value=300)

# String variables for label text
damage_str = tk.StringVar(value='Damage = 100')
max_traj_str = tk.StringVar(value='Max Trajectory = 300')

# Labels for sliders
damage_label = tk.Label(root, textvariable=damage_str)
max_traj_label = tk.Label(root, textvariable=max_traj_str)

# Slider widgets  
damage_slider = ttk.Scale(root, from_=1, to=10000, 
                          variable=damage_var, orient=tk.VERTICAL)

max_traj_slider = ttk.Scale(root, from_=1, to=10000, 
                            variable=max_traj_var, orient=tk.VERTICAL)

# Functions to update labels when sliders change  
def update_damage(event):
  damage_str.set(f'Damage = {damage_var.get()}')

def update_max_traj(event):
  max_traj_str.set(f'Max Trajectory = {max_traj_var.get()}')
  
# Bind slider motion to update functions  
damage_slider.bind("<Motion>", update_damage)
max_traj_slider.bind("<Motion>", update_max_traj)

# Pack labels and sliders
damage_label.pack()
damage_slider.pack(fill='x')  

max_traj_label.pack()
max_traj_slider.pack(fill='x')

# Save button click handler
def save_config():

  # Get current values
  damage = damage_var.get()
  max_traj = max_traj_var.get()

  # Open file and modify
  with open('testconfig.cs', 'r') as f:
    
    contents = re.sub('BaseDamage = [0-9]*,',  
                      f'BaseDamage = {damage},', f.read())
                      
    contents = re.sub('MaxTrajectory = [0-9]*,',  
                      f'MaxTrajectory = {max_traj},', contents)

  # Save changes 
  with open('testconfig.cs', 'w') as f:
    f.write(contents)
  
  # Update text box
  text.config(state='normal')
  text.delete('1.0', 'end')
  text.insert('1.0', open('testconfig.cs').read())
  text.config(state='disabled')
  
# Save button
button = tk.Button(root, text="Save", command=save_config)
button.pack()

# Text box
text = tk.Text(root)
text.pack(fill='both', expand=True)
text.insert('1.0', open('testconfig.cs').read())
text.config(state='disabled')

root.mainloop()