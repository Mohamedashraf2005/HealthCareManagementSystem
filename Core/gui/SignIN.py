from tkinter import Label, Button, Entry, Frame, DISABLED, NORMAL
from PIL import Image, ImageTk
from SignUP import SignUp
from AdminDashboard import AdminDashboard
from Doctor_Dpage import DoctorPage
from patient_Dpage import PatientPage
import dbfunctions as dbf
import os
import sqlite3
from tkinter import messagebox
import customtkinter as ctk


#if you want connect with database write inside connect (db_path) مهم مهم مهم مهم مهم 
db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'HCMSclinic.db')

def get_resource_path(*path_parts):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, *path_parts)

class LogIn:
    def __init__(self, container, app):
        """Initialize the login page frame and setup all UI components."""
        # Create frame within the container
        print("\nDEBUG  login HEREEEEE######\n")
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
        self.login_buttonA =None
        self.login_buttonP =None
        self.login_buttonD =None

        # Call methods to build the UI
        self.logo_image()
        self.create_buttons()
        self.create_login_form()

    def logo_image(self):
        image = Image.open(get_resource_path("PHOTO", "logo.png")).resize((110, 100)).convert("RGBA")
        datas = image.getdata()
        new_data = []
        for item in datas:
            if item[0] > 200 and item[1] > 200 and item[2] > 200:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
        image.putdata(new_data)
        image = ImageTk.PhotoImage(image)
        label = Label(self.frame, text='DocHub', compound="top", image=image, borderwidth=0,
                      font=("IM FELL Double Pica", 13, "bold"), bg="#B5B9F1", fg='#194C7C')
        label.image = image
        label.place(x=0, y=0)
        return label

    def show_login(self, title):
        """Update the login section to display data specific to the selected role"""
        self.login_title.config(text=f"{title} Login")
        self.username_entry.config(state=NORMAL)  # Enable the username field
        self.password_entry.config(state=NORMAL)  # Enable the password field
        self.username_entry.delete(0, 'end')  # Clear the username field
        self.password_entry.delete(0, 'end')  # Clear the password field
        self.error_message.config(text="")  # Hide the error message
        #####ya rab sabarny
        # Show or hide the "Sign Up?" button based on the account type
        if title == "Patient":
            self.login_buttonP.place(x=590, y=620) 
            self.sign_up_button.place(x=590, y=660)  # Show "Sign Up?" button for "Patient"
        else:
            self.sign_up_button.place_forget()  # Hide "Sign Up?" button for other roles
            self.login_buttonP.place_forget()  # Hide "Sign Up?" button for other roles
      
        if title == "Doctor":
            self.login_buttonD.place(x=590, y=620)  # Show "Sign Up?" button for "Patient"
        else:
            self.login_buttonD.place_forget()  # Hide "Sign Up?" button for other roles
        
        if title == "Admin":
            self.login_buttonA.place(x=590, y=620)  # Show "Sign Up?" button for "Patient"
        else:
            self.login_buttonA.place_forget()  # Hide "Sign Up?" button for other roles
        #####
        # login_button = Button(self.frame, text="Login", font=("Arial", 12, "bold"), 
        #                        bg="#8A8EBF", fg="white", width=10, command=self.attempt_login)
        # login_button.place(x=590, y=620)


        ########################
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
        #.open(get_resource_path("PHOTO", "logo.png"))
        self.create_button_with_frame(get_resource_path("PHOTO", "patain.jpg"), "Patient", x=350, y=200, 
                                       command=lambda: self.show_login("Patient"))
        self.create_button_with_frame(get_resource_path("PHOTO", "doctorimage.jpg"), "Doctor", x=550, y=200, 
                                       command=lambda: self.show_login("Doctor"))
        self.create_button_with_frame(get_resource_path("PHOTO", "admin.jpg"), "Admin", x=750, y=200, 
                                       command=lambda: self.show_login("Admin"))
    

    def create_login_form(self):
        """Create the login form with username, password fields and login button"""
        # Login Title
        self.login_title = Label(self.frame, text="Select Type", font=("Arial", 18, "bold"), bg="#B5B9F1")
        self.login_title.place(x=565, y=400)

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
        # login_button = Button(self.frame, text="Login", font=("Arial", 12, "bold"), 
        #                        bg="#8A8EBF", fg="white", width=10, command=self.attempt_login)
        # login_button.place(x=590, y=620)

        # Sign Up Button
        self.sign_up_button = Button(self.frame, text="Sign Up?", font=("Arial", 12, "bold"), 
                                      bg="#8A8EBF", fg="white", width=10, 
                                      command=self.sign_up)
        
        self.login_buttonA = Button(self.frame, text="Log in", font=("Arial", 12, "bold"), 
                                      bg="#8A8EBF", fg="white", width=10,
                                      command=self.attempt_loginA 
                                     )
        
        self.login_buttonP = Button(self.frame, text="Log in", font=("Arial", 12, "bold"), 
                                      bg="#8A8EBF", fg="white", width=10, 
                                      command=self.attempt_loginP)
        
        self.login_buttonD = Button(self.frame, text="Log in", font=("Arial", 12, "bold"), 
                                      bg="#8A8EBF", fg="white", width=10, 
                                      command=self.attempt_loginD)



    def validate_account_selection(self):
        """Ensure the user has selected an account type before interacting with fields or clicking Login"""
        if self.login_title.cget("text") == "Login":
            self.error_message.config(text="Please select an account type first.")
            return False
        return True

    def attempt_loginP(self):
        """Check if an account type has been selected before attempting to log in"""
        if self.validate_account_selection():
            # Add the code here for login verification
            if dbf.check_username(self.username_entry.get()) and dbf.check_password(self.username_entry.get(),self.password_entry.get()):
                patientuser_data = dbf.usernametodahboarf(self.username_entry.get())
                # addditontemp="40"
                
                OTP=dbf.returnidlolo(patientuser_data)
                
                # OTP=465465;
                message = f"""
            Your verification code is:
                    {OTP}
                Use this code to complete your login. If you did not request this, please ignore this message.
                """
                messagebox.showinfo("Two-Factor Authentication", message)
              
                print(f"DEBUG HERE!####################patient data returned: {patientuser_data}#########")
                self.app.show_frame(PatientPage)
            else:
                self.error_message.config(text="Wrong username or Password,Try Again!")  # Hide the error message if login is successful

    def attempt_loginD(self):
        """Check if an account type has been selected before attempting to log in"""
        if self.validate_account_selection():
            # Add the code here for login verification
            if dbf.check_usernameD(self.username_entry.get()) and dbf.check_passwordD(self.username_entry.get(),self.password_entry.get()):
               self.app.show_frame(DoctorPage)
               doctoruser_data=dbf.usernametodahboardoctor(self.username_entry.get())
               print(f"DEBUG HERE!####################doctor data returned: {doctoruser_data}#########")
               OTP=dbf.returnidnono(doctoruser_data)
                
                # OTP=465465;
               messagedoc = f"""
                Your verification code is:
                        {OTP}
                    Use this code to complete your login. If you did not request this, please ignore this message.
                    """
               messagebox.showinfo("Two-Factor Authentication", messagedoc)
              
               self.app.show_frame(DoctorPage)
            
            else:
                self.error_message.config(text="Wrong doctor or Password,Try Again!")  # Hide the error message if login is successful

    def attempt_loginA(self):
        """Check if an account type has been selected before attempting to log in"""
        if self.validate_account_selection():
            # Add the code here for login verification
            if self.username_entry.get() =="admin" and self.password_entry.get()=="1234":
                # print("succesfully ya 3alamy")
                self.app.show_frame(AdminDashboard)
            else:
                self.error_message.config(text="Wrong admin or Password,Try Again!")  # Hide the error message if login is successful


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