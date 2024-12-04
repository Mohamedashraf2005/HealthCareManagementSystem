from tkinter import Tk, Label, Button, Entry, Frame, DISABLED, NORMAL
from PIL import Image, ImageTk


root = Tk()
root.geometry("1200x950")  
root.configure(bg="#B5B9F1")  
root.title("Log In")
root.resizable(False, False)   

# Function for Logo
def logo_image():
    """Add the logo at the top"""
    image = Image.open("logo.png").resize((150, 100))
    image = ImageTk.PhotoImage(image)
    label = Label(root, text="BANANA CLINIC", compound="top", image=image, borderwidth=0, 
                  font=("IM FELL Double Pica", 15, "bold"), bg="#B5B9F1")
    label.image = image
    label.place(x=10, y=0)
    return label


logo_img = logo_image()

def show_login(title):
    """Update the login section to display data specific to the selected role"""
    login_title.config(text=f"{title} Login")   
    username_entry.config(state=NORMAL)  # Enable the username field
    password_entry.config(state=NORMAL)  # Enable the password field
    username_entry.delete(0, 'end')  # Clear the username field
    password_entry.delete(0, 'end')  # Clear the password field
    error_message.config(text="")  # Hide the error message

    # Show or hide the "Sign Up?" button based on the account type
    if title == "Patient":
        sign_up_button.place(x=590, y=660)  # Show "Sign Up?" button for "Patient"
    else:
        sign_up_button.place_forget()  # Hide "Sign Up?" button for other roles

def create_button_with_frame(image_path, text, x, y, command):
    frame = Frame(root, bg="#8A8EBF", width=120, height=150) 
    frame.place(x=x, y=y)
    
    img = Image.open(image_path).resize((100, 100))
    img = ImageTk.PhotoImage(img)
    
    button = Button(frame, text=text, compound="top", image=img, bg="#B5B9F1", borderwidth=0, 
                    font=("Arial", 10, "bold"), command=command)
    button.image = img  # Prevent image deletion from memory
    button.place(x=10, y=10)  

# Buttons with frames
create_button_with_frame("patain.jpg", "Patient", x=350, y=200, command=lambda: show_login("Patient"))
create_button_with_frame("doctorimage.jpg", "Doctor", x=550, y=200, command=lambda: show_login("Doctor"))
create_button_with_frame("admin.jpg", "Admin", x=750, y=200, command=lambda: show_login("Admin"))

login_title = Label(root, text="Login", font=("Arial", 18, "bold"), bg="#B5B9F1")
login_title.place(x=575, y=400)  

Label(root, text="Username", font=("Arial", 12), bg="#B5B9F1").place(x=410, y=480)  # Username text
username_entry = Entry(root, width=30, font=("Arial", 12), state=DISABLED)  # Initially disabled field
username_entry.place(x=510, y=480)  # Username entry field

Label(root, text="Password", font=("Arial", 12), bg="#B5B9F1").place(x=410, y=530)  # Password text
password_entry = Entry(root, width=30, font=("Arial", 12), show="*", state=DISABLED)  # Initially disabled field
password_entry.place(x=510, y=530)  # Password entry field

# Error message
error_message = Label(root, text="", font=("Arial", 12, "bold"), fg="red", bg="#B5B9F1")
error_message.place(x=515, y=575)  # Place the error message below the login button

# Function to validate account type selection before attempting login or interacting with fields
def validate_account_selection():
    """Ensure the user has selected an account type before interacting with fields or clicking Login"""
    if login_title.cget("text") == "Login":
        error_message.config(text="Please select an account type first.")
        return False
    return True

# Login button
def attempt_login():
    """Check if an account type has been selected before attempting to log in"""
    if validate_account_selection():
        # Add the code here for login verification
        error_message.config(text="")  # Hide the error message if login is successful

login_button = Button(root, text="Login", font=("Arial", 12, "bold"), bg="#8A8EBF", fg="white", width=10, command=attempt_login)
login_button.place(x=590, y=620)  # Login button

# Interact with input fields (username and password) separately
def on_entry_click(event):
    """Handle interaction with input fields before account type selection"""
    if not validate_account_selection():
        # If account type is not selected, display an error message
        error_message.config(text="Please select an account type first.")
        event.widget.delete(0, 'end')  # Clear the field upon interaction

# Bind events to input fields
username_entry.bind("<FocusIn>", on_entry_click)  # On clicking the username field
password_entry.bind("<FocusIn>", on_entry_click)  # On clicking the password field

# Function to navigate the user to the signup page when "Sign Up?" is clicked
def sign_up():
    """Function executed when "Sign Up?" button is clicked"""
    error_message.config(text="You can sign up as a patient.")

# "Sign Up?" button
sign_up_button = Button(root, text="Sign Up?", font=("Arial", 12, "bold"), bg="#8A8EBF", fg="white", width=10, command=sign_up)

# Back button
btn1 = Button(root, text="<back", font=("IM FELL Double Pica", 15, "bold"), 
              fg="SteelBlue", bg="#B5B9F1", borderwidth=0)
btn1.place(x=1125, y=10)

root.mainloop()
