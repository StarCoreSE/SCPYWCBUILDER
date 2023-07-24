import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import re

# Root window
root = tk.Tk()
root.title("Ammo Editor")

# Initialize selected_file_path to None
selected_file_path = None

def read_current_values(file_path):
    # Open file and read the contents
    with open(file_path, 'r') as f:
        contents = f.read()

    # Check if the file contains the AmmoDef identifier
    if "AmmoDef" not in contents:
        messagebox.showwarning("Warning", "The selected file is not a valid ammo config.")
        return

    # Find the values using regular expressions
    damage = re.search(r'BaseDamage = (\d+)', contents)
    max_traj = re.search(r'MaxTrajectory = (\d+)', contents)
    desired_speed = re.search(r'DesiredSpeed = (\d+)', contents)
    color = re.search(r'Color = Color\(red: (\d+), green: (\d+), blue: (\w+), alpha: (\d+)\)', contents)

    # Update the slider variables with the found values
    if damage:
        damage_var.set(int(damage.group(1)))
    else:
        messagebox.showwarning("Warning", "Damage value not found in the file.")
    if max_traj:
        max_traj_var.set(int(max_traj.group(1)))
    else:
        messagebox.showwarning("Warning", "Max trajectory value not found in the file.")
    if desired_speed:
        desired_speed_var.set(int(desired_speed.group(1)))
    else:
        messagebox.showwarning("Warning", "Desired speed value not found in the file.")
    if color:
        color_red_var.set(color.group(1))
        color_green_var.set(color.group(2))
        color_blue_var.set(color.group(3))
        color_alpha_var.set(color.group(4))


# Function to validate integer input in entry fields
def validate_integer_input(var, index, value, action):
    if value.isdigit() or (value == "" and action == "1"):  # Allow empty string when deleting
        return True
    return False

# Function to update the color preview
def update_color_preview():
    red = min(max(int(color_red_var.get()), 0), 255)
    green = min(max(int(color_green_var.get()), 0), 255)
    blue = min(max(int(color_blue_var.get()), 0), 255)
    color_preview_canvas.config(bg=f'#{red:02x}{green:02x}{blue:02x}')


# Variables to store values
damage_var = tk.IntVar(value=100)
max_traj_var = tk.IntVar(value=300)
desired_speed_var = tk.IntVar(value=50)
color_red_var = tk.StringVar(value='5')
color_green_var = tk.StringVar(value='2')
color_blue_var = tk.StringVar(value='1')
color_alpha_var = tk.StringVar(value='1')

# Function to open file selector and read the selected file
def open_file():
    global selected_file_path
    file_path = filedialog.askopenfilename(initialdir=os.path.join(os.getcwd()), title="Select Ammo Config File", filetypes=(("CS files", "*.cs"), ("All files", "*.*")))
    
    if file_path:
        selected_file_path = file_path
        read_current_values(file_path)

        # Update text box
        text.config(state='normal')
        text.delete('1.0', 'end')
        text.insert('1.0', open(file_path).read())
        text.config(state='disabled')
    else:
        selected_file_path = None  # Set selected_file_path to None if the user cancels the file dialog

# Function to check if a default_ammo.cs file exists in the config folder
def check_default_ammo_file():
    global default_file_path  # Declare default_file_path as global
    config_folder = os.path.join(os.getcwd(), "config")
    default_file_path = os.path.join(config_folder, "default_ammo.cs")

    if os.path.exists(default_file_path):
        read_current_values(default_file_path)
        selected_file_path = default_file_path
    else:
        messagebox.showinfo("Info", "Please grab the default_ammo.cs file in the 'config' folder and rename it to something unique.")

# Button to open file selector
open_button = ttk.Button(root, text="Open Ammo Config File", command=open_file)
open_button.grid(row=0, column=0, columnspan=7, padx=10, pady=5)

# Read current values from the default configuration file
check_default_ammo_file()


def check_for_cs_files():
    cs_files = [file for file in os.listdir() if file.endswith(".cs")]
    if not cs_files:
        messagebox.showwarning("Warning", "There are no .cs files in the program directory. Please copy an ammo config file (e.g., default_ammo.cs) and name it something unique.")

# Button to open file selector
open_button = ttk.Button(root, text="Open Ammo Config File", command=open_file)
open_button.grid(row=0, column=0, columnspan=7, padx=10, pady=5)

# Check for .cs files in the program directory
check_for_cs_files()

# String variables for label text
damage_str = tk.StringVar(value=f'Damage = {damage_var.get()}')
max_traj_str = tk.StringVar(value=f'Max Trajectory = {max_traj_var.get()}')
desired_speed_str = tk.StringVar(value=f'Desired Speed = {desired_speed_var.get()}')
color_str = tk.StringVar(value=f'Color = Color(red: {color_red_var.get()}, green: {color_green_var.get()}, blue: {color_blue_var.get()}, alpha: {color_alpha_var.get()})')

# Labels for sliders and color
damage_label = tk.Label(root, textvariable=damage_str)
max_traj_label = tk.Label(root, textvariable=max_traj_str)
desired_speed_label = tk.Label(root, textvariable=desired_speed_str)
color_label = tk.Label(root, textvariable=color_str)

# Slider widgets
damage_slider = ttk.Scale(root, from_=1, to=10000, variable=damage_var, orient=tk.HORIZONTAL)
max_traj_slider = ttk.Scale(root, from_=1, to=10000, variable=max_traj_var, orient=tk.HORIZONTAL)
desired_speed_slider = ttk.Scale(root, from_=1, to=10000, variable=desired_speed_var, orient=tk.HORIZONTAL)

# Color entry boxes
color_entry_label = tk.Label(root, text="R, G, B:")
color_red_entry = ttk.Entry(root, textvariable=color_red_var, width=5, validate='key')
color_red_entry['validatecommand'] = (root.register(validate_integer_input), '%v', '%i', '%P', '%d')
color_red_entry.bind("<FocusOut>", lambda event: update_color_preview())
color_red_entry.bind("<KeyRelease>", lambda event: update_color_preview())  # Update on key release

color_green_entry = ttk.Entry(root, textvariable=color_green_var, width=5, validate='key')
color_green_entry['validatecommand'] = (root.register(validate_integer_input), '%v', '%i', '%P', '%d')
color_green_entry.bind("<FocusOut>", lambda event: update_color_preview())
color_green_entry.bind("<KeyRelease>", lambda event: update_color_preview())  # Update on key release

color_blue_entry = ttk.Entry(root, textvariable=color_blue_var, width=5, validate='key')
color_blue_entry['validatecommand'] = (root.register(validate_integer_input), '%v', '%i', '%P', '%d')
color_blue_entry.bind("<FocusOut>", lambda event: update_color_preview())
color_blue_entry.bind("<KeyRelease>", lambda event: update_color_preview())  # Update on key release

color_alpha_label = tk.Label(root, text="Alpha:")
color_alpha_entry = ttk.Entry(root, textvariable=color_alpha_var, width=5, validate='key')
color_alpha_entry['validatecommand'] = (root.register(validate_integer_input), '%v', '%i', '%P', '%d')
color_alpha_entry.bind("<FocusOut>", lambda event: update_color_preview())
color_alpha_entry.bind("<KeyRelease>", lambda event: update_color_preview())  # Update on key release

# Function to update labels when sliders change
def update_damage(event):
    damage_str.set(f'Damage = {damage_var.get()}')

def update_max_traj(event):
    max_traj_str.set(f'Max Trajectory = {max_traj_var.get()}')

def update_desired_speed(event):
    desired_speed_str.set(f'Desired Speed = {desired_speed_var.get()}')

# Bind slider motion to update functions
damage_slider.bind("<Motion>", update_damage)
max_traj_slider.bind("<Motion>", update_max_traj)
desired_speed_slider.bind("<Motion>", update_desired_speed)

# Function to increment slider by one using mouse wheel
def increment_slider(event):
    if event.delta > 0:
        event.widget.set(event.widget.get() + 1)
    elif event.delta < 0:
        event.widget.set(event.widget.get() - 1)

    # Update labels in real-time
    update_damage(event)
    update_max_traj(event)
    update_desired_speed(event)

# Bind mouse wheel event to sliders
damage_slider.bind("<MouseWheel>", increment_slider)
max_traj_slider.bind("<MouseWheel>", increment_slider)
desired_speed_slider.bind("<MouseWheel>", increment_slider)

# Pack labels and sliders using grid layout
damage_label.grid(row=1, column=0, padx=10, pady=5)
damage_slider.grid(row=2, column=0, padx=10, pady=5)

max_traj_label.grid(row=1, column=1, padx=10, pady=5)
max_traj_slider.grid(row=2, column=1, padx=10, pady=5)

desired_speed_label.grid(row=1, column=2, padx=10, pady=5)
desired_speed_slider.grid(row=2, column=2, padx=10, pady=5)

color_label.grid(row=1, column=3, padx=10, pady=5)
color_entry_label.grid(row=2, column=3, padx=10, pady=5)
color_red_entry.grid(row=2, column=4, padx=2, pady=5)
color_green_entry.grid(row=2, column=5, padx=2, pady=5)
color_blue_entry.grid(row=2, column=6, padx=2, pady=5)

color_alpha_label.grid(row=3, column=3, padx=10, pady=5)
color_alpha_entry.grid(row=3, column=4, padx=2, pady=5)

# Color preview canvas
color_preview_label = tk.Label(root, text="Color Preview:")
color_preview_canvas = tk.Canvas(root, width=30, height=30, bg='white')
color_preview_label.grid(row=3, column=5, padx=10, pady=5)
color_preview_canvas.grid(row=3, column=6, padx=2, pady=5)

# Save button click handler
def save_config():

    global selected_file_path
    if selected_file_path is None:
        messagebox.showerror("Error", "No file is currently loaded. Please open an ammo config file first.")
        return
    
    # Get current values
    damage = damage_var.get()
    max_traj = max_traj_var.get()
    desired_speed = desired_speed_var.get()
    color_red = color_red_var.get()
    color_green = color_green_var.get()
    color_blue = color_blue_var.get()
    color_alpha = color_alpha_var.get()

    # Format the color string
    color_str.set(f'Color = Color(red: {color_red}, green: {color_green}, blue: {color_blue}, alpha: {color_alpha})')

    # Open file and modify
    with open(selected_file_path, 'r') as f:
        contents = re.sub('BaseDamage = [0-9]*,', f'BaseDamage = {damage},', f.read())
        contents = re.sub('MaxTrajectory = [0-9]*,', f'MaxTrajectory = {max_traj},', contents)
        contents = re.sub('DesiredSpeed = [0-9]*,', f'DesiredSpeed = {desired_speed},', contents)
        contents = re.sub('Color = Color\(red: [0-9a-z]*,', f'Color = Color(red: {color_red},', contents)
        contents = re.sub('green: [0-9a-z]*,', f'green: {color_green},', contents)
        contents = re.sub('blue: [0-9a-z]*,', f'blue: {color_blue},', contents)
        contents = re.sub('alpha: [0-9]*\),', f'alpha: {color_alpha}),', contents)

    # Save changes
    with open(selected_file_path, 'w') as f:
        f.write(contents)

    # Update text box
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.insert('1.0', open(selected_file_path).read())
    text.config(state='disabled')

# Save button
button = tk.Button(root, text="Save", command=save_config)
button.grid(row=4, column=0, columnspan=7, padx=10, pady=5)

# Text box
text = tk.Text(root)
text.grid(row=5, column=0, columnspan=7, padx=10, pady=5, sticky="nsew")


# Update the text box display based on whether a file is loaded or not
def update_text_display():
    if selected_file_path:
        text.config(state='normal')
        text.delete('1.0', 'end')
        text.insert('1.0', open(selected_file_path).read())
        text.config(state='disabled')
    else:
        text.config(state='normal')
        text.delete('1.0', 'end')
        text.config(state='disabled')

# Configure grid weights to make the text box expand when the window is resized
for i in range(7):
    root.grid_columnconfigure(i, weight=1)

# Call update_text_display to initialize the text box display
update_text_display()

root.grid_rowconfigure(5, weight=1)

root.mainloop()
