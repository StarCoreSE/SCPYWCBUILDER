import tkinter as tk
from tkinter import ttk
import os

# Function to launch the Fixed Weapon Editor
def launch_fixed_weapon_editor():
    os.system("python visualfixedweaponeditor.py")

# Function to launch the Turreted Weapon Editor
def launch_turreted_weapon_editor():
    os.system("python visualturretedweaponeditor.py")

# Function to launch the Ammo Editor
def launch_ammo_editor():
    os.system("python visualammoeditor.py")

# Root window
root = tk.Tk()
root.title("Launcher")

# Set the initial window size (width x height)
window_width = 200
window_height = 250
root.geometry(f"{window_width}x{window_height}")

# Button to run the Fixed Weapon Editor
fixed_weapon_editor_button = ttk.Button(root, text="Run Fixed Weapon Editor", command=launch_fixed_weapon_editor)
fixed_weapon_editor_button.pack(pady=20)

# Button to run the Turreted Weapon Editor
turreted_weapon_editor_button = ttk.Button(root, text="Run Turreted Weapon Editor", command=launch_turreted_weapon_editor)
turreted_weapon_editor_button.pack(pady=20)

# Button to run the Ammo Editor
ammo_editor_button = ttk.Button(root, text="Run Ammo Editor", command=launch_ammo_editor)
ammo_editor_button.pack(pady=20)

root.mainloop()
