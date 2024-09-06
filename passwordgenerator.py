import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_random_password(length=16):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    all_characters = lower + upper + digits + special
    
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    password += random.choices(all_characters, k=length-4)
    
    random.shuffle(password)
    
    return ''.join(password)

def on_generate_password():
    try:
        length = int(password_length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return
        
        password = generate_random_password(length)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length")

window = tk.Tk()
window.title("Random Password Generator")
window.geometry("400x200")

password_length_label = tk.Label(window, text="Enter password length:")
password_length_label.pack(pady=10)

password_length_entry = tk.Entry(window, width=10)
password_length_entry.pack(pady=5)

generate_button = tk.Button(window, text="Generate Password", command=on_generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
