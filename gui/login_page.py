from tkinter import Tk, Label, Button, Entry, Frame, DISABLED, NORMAL
from PIL import Image, ImageTk

class LogIn:
    def __init__(self, root):
        """Initialize the main window and setup all UI components."""
        self.root = root
        self.root.geometry("1200x750+150+25")
        self.root.configure(bg="#B5B9F1")
        self.root.title("Log In")
        self.root.resizable(False, False)

        # Call methods to build the UI
        self.logo_image()
        self.create_buttons()
        self.create_login_form()
        self.create_back_button()

    def logo_image(self):
        """Add the logo at the top"""
        image = Image.open("logo.png").resize((150, 100))
        image = ImageTk.PhotoImage(image)
        label = Label(self.root, text="DocHub", compound="top", image=image, borderwidth=0,
                      font=("IM FELL Double Pica", 15, "bold"), bg="#B5B9F1")
        label.image = image  # Prevent image deletion from memory
        label.place(x=10, y=0)
        return label

    def show_login(self, title):
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

    def create_button_with_frame(self, image_path, text, x, y, command):
        """Helper function to create buttons with frames"""
        frame = Frame(self.root, bg="#8A8EBF", width=120, height=150)
        frame.place(x=x, y=y)

        img = Image.open(image_path).resize((100, 100))
        img = ImageTk.PhotoImage(img)

        button = Button(frame, text=text, compound="top", image=img, bg="#B5B9F1", borderwidth=0,
                        font=("Arial", 10, "bold"), command=command)
        button.image = img  # Prevent image deletion from memory
        button.place(x=10, y=10)

    def create_buttons(self):
        """Create the account type selection buttons"""
        self.create_button_with_frame("patain.jpg", "Patient", x=350, y=200, command=lambda: self.show_login("Patient"))
        self.create_button_with_frame("doctorimage.jpg", "Doctor", x=550, y=200, command=lambda: self.show_login("Doctor"))
        self.create_button_with_frame("admin.jpg", "Admin", x=750, y=200, command=lambda: self.show_login("Admin"))

    def create_login_form(self):
        """Create the login form with username, password fields and login button"""
        global login_title, username_entry, password_entry, error_message, sign_up_button

        login_title = Label(self.root, text="Login", font=("Arial", 18, "bold"), bg="#B5B9F1")
        login_title.place(x=575, y=400)

        Label(self.root, text="Username", font=("Arial", 12), bg="#B5B9F1").place(x=410, y=480)  # Username text
        username_entry = Entry(self.root, width=30, font=("Arial", 12), state=DISABLED)  # Initially disabled field
        username_entry.place(x=510, y=480)  # Username entry field

        Label(self.root, text="Password", font=("Arial", 12), bg="#B5B9F1").place(x=410, y=530)  # Password text
        password_entry = Entry(self.root, width=30, font=("Arial", 12), show="*", state=DISABLED)  # Initially disabled field
        password_entry.place(x=510, y=530)  # Password entry field

        # Error message
        error_message = Label(self.root, text="", font=("Arial", 12, "bold"), fg="red", bg="#B5B9F1")
        error_message.place(x=515, y=575)  # Place the error message below the login button

        # Login button
        login_button = Button(self.root, text="Login", font=("Arial", 12, "bold"), bg="#8A8EBF", fg="white", width=10, command=self.attempt_login)
        login_button.place(x=590, y=620)  # Login button

        # Sign Up? button
        sign_up_button = Button(self.root, text="Sign Up?", font=("Arial", 12, "bold"), bg="#8A8EBF", fg="white", width=10, command=self.sign_up)

    def create_back_button(self):
        """Create the back button"""
        btn1 = Button(self.root, text="<back", font=("IM FELL Double Pica", 15, "bold"),
                      fg="SteelBlue", bg="#B5B9F1", borderwidth=0)
        btn1.place(x=1125, y=10)

    def validate_account_selection(self):
        """Ensure the user has selected an account type before interacting with fields or clicking Login"""
        if login_title.cget("text") == "Login":
            error_message.config(text="Please select an account type first.")
            return False
        return True

    def attempt_login(self):
        """Check if an account type has been selected before attempting to log in"""
        if self.validate_account_selection():
            # Add the code here for login verification
            error_message.config(text="")  # Hide the error message if login is successful

    def on_entry_click(self, event):
        """Handle interaction with input fields before account type selection"""
        if not self.validate_account_selection():
            # If account type is not selected, display an error message
            error_message.config(text="Please select an account type first.")
            event.widget.delete(0, 'end')  # Clear the field upon interaction

    def sign_up(self):
        """Function executed when "Sign Up?" button is clicked"""
        error_message.config(text="You can sign up as a patient.")


if __name__ == "__main__":
    root = Tk()
    log_in_page = LogIn(root)
    root.mainloop()