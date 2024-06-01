import tkinter as tk
from tkinter import messagebox
import random
import string
from tkinter import *


def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password
    

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

def generate_and_display_password(length):
    password = generate_password(length)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def update_length_label(length):
    length_label.config(text=f"Length: {length}")

root = tk.Tk()
root.title("Password Generator")

root.geometry("700x350")

px=30
py=30

frame=Frame(root, width=40, height=65)

label=Label(frame, text="Password Generator", font=('Arial 15 bold'))
label.pack(padx=px, pady=py)
frame.pack(padx=px, pady=py)


length_label = tk.Label(root, text="Length: 8")
length_label.pack()


length_scale = tk.Scale(root, from_=8, to=30, orient=tk.HORIZONTAL, command=update_length_label)
length_scale.pack()

generate_button = tk.Button(root, text="Generate", command=lambda: generate_and_display_password(length_scale.get()))
generate_button.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, width=30)
password_entry.pack()

copy_button = tk.Button(root, text="Copy", command=copy_password)
copy_button.pack()
root.geometry("400x400")

root.mainloop()