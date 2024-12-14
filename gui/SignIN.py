from tkinter import Label, Button, Entry, Frame, DISABLED, NORMAL
from PIL import Image, ImageTk
from SignUP import SignUp
import sqlite3
import dbfunctions as dbf
class LogIn:
    def __init__(self, container, app):
        """Initialize the login page frame and setup all UI components."""
        # Create frame within the container
        self.frame = Frame(container, width=1200, height=750, bg="#B5B9F1")
        self.frame.grid(row=0, column=0, sticky="nsew")
        
        # Store reference to the main application
        self.app = app

        # Global variables for dynamic widgets
        self.login_title = None
        self.username_entry = None
        self.password_entry = None
        self.error_message = None
        self.sign_up_button = None

        # Call methods to build the UI
        self.logo_image()
        self.create_buttons()
        self.create_login_form()
        self.create_back_button()

    def logo_image(self):
        """Add the logo at the top"""
        image = Image.open("logo.png").resize((110, 100))
        image = ImageTk.PhotoImage(image)
        label = Label(self.frame, text="DocHub", compound="top", image=image, borderwidth=0,
                      font=("IM FELL Double Pica", 13, "bold"), bg="#B5B9F1",fg='#194C7C')
        label.image = image  # Prevent image deletion from memory
        label.place(x=10, y=0)
        return label

    def show_login(self, title):
        """Update the login section to display data specific to the selected role"""
        self.login_title.config(text=f"{title} Login")
        self.username_entry.config(state=NORMAL)  # Enable the username field
        self.password_entry.config(state=NORMAL)  # Enable the password field
        self.username_entry.delete(0, 'end')  # Clear the username field
        self.password_entry.delete(0, 'end')  # Clear the password field
        self.error_message.config(text="")  # Hide the error message

        # Show or hide the "Sign Up?" button based on the account type
        if title == "Patient":
            self.sign_up_button.place(x=590, y=660)  # Show "Sign Up?" button for "Patient"
        else:
            self.sign_up_button.place_forget()  # Hide "Sign Up?" button for other roles

    def create_button_with_frame(self, image_path, text, x, y, command):
        """Helper function to create buttons with frames"""
        frame = Frame(self.frame, bg="#8A8EBF", width=120, height=150)
        frame.place(x=x, y=y)

        img = Image.open(image_path).resize((100, 100))
        img = ImageTk.PhotoImage(img)

        button = Button(frame, text=text, compound="top", image=img, bg="#B5B9F1", borderwidth=0,
                        font=("Arial", 10, "bold"), command=command)
        button.image = img  # Prevent image deletion from memory
        button.place(x=10, y=10)

    def create_buttons(self):
        """Create the account type selection buttons"""
        self.create_button_with_frame("patain.jpg", "Patient", x=350, y=200, 
                                       command=lambda: self.show_login("Patient"))
        self.create_button_with_frame("doctorimage.jpg", "Doctor", x=550, y=200, 
                                       command=lambda: self.show_login("Doctor"))
        self.create_button_with_frame("admin.jpg", "Admin", x=750, y=200, 
                                       command=lambda: self.show_login("Admin"))

    def create_login_form(self):
        """Create the login form with username, password fields and login button"""
        # Login Title
        self.login_title = Label(self.frame, text="Login", font=("Arial", 18, "bold"), bg="#B5B9F1")
        self.login_title.place(x=575, y=400)

        # Username Label and Entry
        Label(self.frame, text="Username", font=("Arial", 12), bg="#B5B9F1").place(x=410, y=480)
        self.username_entry = Entry(self.frame, width=30, font=("Arial", 12), state=DISABLED)
        self.username_entry.place(x=510, y=480)

        # Password Label and Entry
        Label(self.frame, text="Password", font=("Arial", 12), bg="#B5B9F1").place(x=410, y=530)
        self.password_entry = Entry(self.frame, width=30, font=("Arial", 12), show="*", state=DISABLED)
        self.password_entry.place(x=510, y=530)

        # Error Message
        self.error_message = Label(self.frame, text="", font=("Arial", 12, "bold"), 
                                    fg="red", bg="#B5B9F1")
        self.error_message.place(x=515, y=575)

        # Login Button
        login_button = Button(self.frame, text="Login", font=("Arial", 12, "bold"), 
                               bg="#8A8EBF", fg="white", width=10, command=self.attempt_login)
        login_button.place(x=590, y=620)

        # Sign Up Button
        self.sign_up_button = Button(self.frame, text="Sign Up?", font=("Arial", 12, "bold"), 
                                      bg="#8A8EBF", fg="white", width=10, 
                                      command=self.sign_up)

    def create_back_button(self):
        """Create the back button"""
        btn1 = Button(self.frame, text="<back", font=("IM FELL Double Pica", 15, "bold"),
                      fg="SteelBlue", bg="#B5B9F1", borderwidth=0,
                      command=lambda: self.app.show_frame('WelcomePage'))
        btn1.place(x=1125, y=10)

    def validate_account_selection(self):
        """Ensure the user has selected an account type before interacting with fields or clicking Login"""
        if self.login_title.cget("text") == "Login":
            self.error_message.config(text="Please select an account type first.")
            return False
        return True

    def attempt_login(self):
        """Check if an account type has been selected before attempting to log in"""
        if self.validate_account_selection():
            # Add the code here for login verification
            if dbf.check_username(self.username_entry.get()) and dbf.check_password(self.username_entry.get(),self.password_entry.get()):
                print("succesfully")
            else:
                self.error_message.config(text="Wrong username or Password,Try Again!")  # Hide the error message if login is successful

    def on_entry_click(self, event):
        """Handle interaction with input fields before account type selection"""
        if not self.validate_account_selection():
            # If account type is not selected, display an error message
            self.error_message.config(text="Please select an account type first.")
            event.widget.delete(0, 'end')  # Clear the field upon interaction

    def sign_up(self):
        """Function executed when "Sign Up?" button is clicked"""
        self.app.show_frame(SignUp)
        self.error_message.config(text="")

# Commented out main block for standalone testing
# if __name__ == "__main__":
#     root = Tk()
#     root.geometry('1200x750+150+25')
#     root.title('Login Page')
#     root.resizable(False, False)
#     
#     # Create a dummy app class for testing
#     class DummyApp:
#         def show_frame(self, page_name):
#             print(f"Navigating to {page_name}")
#     
#     app = DummyApp()
#     login_page = LogIn(root, app)
#     root.mainloop()