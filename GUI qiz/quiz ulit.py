import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys

# Dictionary to store user accounts (student_id as keys and passwords as values)
user_accounts = {}

# Function to handle login
def login():
    student_id = student_id_entry.get()
    pswd = password_entry.get()
    if student_id not in user_accounts:
        messagebox.showerror("Login Error", "Account or Student ID doesn't exist. Try signing up first.")
    else:
        if user_accounts[student_id] == pswd:
            messagebox.showinfo("Login Successful", "You can now take your quiz.")
            sys.exit()
        else:
            messagebox.showerror("Login Error", "Incorrect password. Please try again.")
            password_entry.delete(0, tk.END)

# Function to handle signup
def signup():
    student_id = student_id_entry.get()
    if student_id in user_accounts:
        messagebox.showerror("Signup Error", "Account already exists. Please login.")
    else:   
        pswd = password_entry.get()
        user_accounts[student_id] = pswd
        messagebox.showinfo("Signup Successful", "Account created successfully. You can now log in.")
        student_id_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

# Function to highlight the button when the cursor enters
def highlight_button(event):
    event.widget.config(bg="lightblue")

# Function to reset the button's background when the cursor leaves
def reset_button(event):
    event.widget.config(bg="SystemButtonFace")

# Function to handle the "Remember Me" checkbox
def remember_me():
    if remember_me_var.get() == 1:
        print("Remember Me Checked")
    else:
        print("Remember Me Unchecked")

# Create the main window
root = tk.Tk()
root.title("Create your Student Account")

# Load and display an image (e.g., a logo) at the top

# Create a frame for the Entry fields and buttons
frame = tk.Frame(root)
frame.pack(side="bottom", fill="both", expand=True)

# Create and place labels and entry fields within the frame
student_id_label = tk.Label(frame, text="STUDENT ID:")
student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

student_id_entry = tk.Entry(frame, width=30)
student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

password_label = tk.Label(frame, text="PASSWORD:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

password_entry = tk.Entry(frame, show="*", width=30)
password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Create login button with hover effect
login_button = tk.Button(frame, text="Login", command=login, width=10, height=2)
login_button.grid(row=2, column=0, columnspan=2, pady=10)
login_button.bind("<Enter>", highlight_button)
login_button.bind("<Leave>", reset_button)

# Create signup button with hover effect
signup_button = tk.Button(frame, text="Signup", command=signup, width=10, height=2)
signup_button.grid(row=3, column=0, columnspan=2, pady=10)
signup_button.bind("<Enter>", highlight_button)
signup_button.bind("<Leave>", reset_button)


# Create a "Remember Me" check button with a variable to track its state
remember_me_var = tk.IntVar()
remember_me_checkbutton = tk.Checkbutton(frame, text="Remember Me", variable=remember_me_var)
remember_me_checkbutton.grid(row=1, column=5, columnspan=15, pady=5)

# Start the GUI application
root.mainloop()