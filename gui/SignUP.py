import sqlite3
from tkinter import messagebox
import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image

# from database.patientslogin import checkname


class SignUp:
    def __init__(self, container, app):
        """Initialize the SignUp page frame and setup all UI components."""
        # Create frame within the container
        self.frame = Frame(container, width=1200, height=750, bg='#B5B9F1')
        self.frame.grid(row=0, column=0, sticky="nsew")

        # Store reference to the main application
        self.app = app

        # Variables to store input values
        self.name_entry = None
        self.password_entry = None
        self.username_entry = None
        self.age_entry = None
        self.phone_entry = None
        self.gender_var = StringVar(value="Male")
        self.warning_label = None  # Warning label for Name validation

        # Initialize UI components
        self.logo_image()
        self.create_sign_in_frame()
        self.create_image_frame()
        # self.create_back_button()

    def create_database(self):
        """Create the SQLite database and table if they do not exist."""
        conn = sqlite3.connect(r"C:\Users\Anas\OneDrive\Desktop\HealthCareManagementSystem\database\HCMSclinic.db")  # Create or connect to the database
        cursor = conn.cursor()

        # Create a table for users
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            username TEXT NOT NULL UNIQUE,
                            age INTEGER,
                            phone TEXT,
                            gender TEXT,
                            password TEXT NOT NULL)''')
        conn.commit()
        conn.close()

    def insert_data_to_db(self, name, username, age, phone, gender, password):
        """Insert user data into the database."""
        try:
            conn = sqlite3.connect(r"C:\Users\Anas\OneDrive\Desktop\HealthCareManagementSystem\database\HCMSclinic.db")
            cursor = conn.cursor()

            # Insert data into the table
            cursor.execute("INSERT INTO users (name, username, age, phone, gender, password) VALUES (?, ?, ?, ?, ?, ?)",
                           (name, username, age, phone, gender, password))
            conn.commit()
            conn.close()
            self.warning_label.config(text="Registration Successful!", fg="green")
        except sqlite3.IntegrityError:
            self.warning_label.config(text="Username already exists!", fg="red")
        except Exception as e:
            self.warning_label.config(text=f"Error: {e}", fg="red")
    
    

    def logo_image(self):
        """Add the logo at the top of the window"""
        image = Image.open("logo.png").resize((150, 100))  # Resize the logo
        image = ImageTk.PhotoImage(image)  # Convert image to Tkinter format
        label = Label(self.frame, text=" ", compound="top", image=image, borderwidth=0,
                      font=("IM FELL Double Pica", 15, "bold"), bg="#B5B9F1")
        label.image = image  # Keep a reference to the image
        label.place(x=10, y=0)  # Position the label
        return label

    def create_sign_in_frame(self):
        """Create the sign-in form with input fields and buttons"""
        f_sign_in = Frame(self.frame, width=600, height=500, bg='#B5B9F1')
        f_sign_in.place(x=200, y=200) #just test by ashraf you could replace it
        lab_sign_in_title = ctk.CTkLabel(f_sign_in, text="Create Account", fg_color='#B5B9F1',
                                         text_color='black', font=('Helvetica', 28))
        lab_sign_in_title.place(x=205, y=0)
        # Create input fields for each user detail
        self.name_entry = self.create_input_field(f_sign_in, "Name", 50)
        self.username_entry = self.create_input_field(f_sign_in, "username", 100)
        self.age_entry = self.create_input_field(f_sign_in, "Age", 150)
        self.phone_entry = self.create_input_field(f_sign_in, "Phone", 200)
        self.password_entry = self.create_input_field(f_sign_in, "Password", 250, show="*")
        # Warning label for name validation
        self.warning_label = Label(f_sign_in, text="", fg="red", bg="#B5B9F1", font=("Arial", 10))
        self.warning_label.place(x=460, y=55)  # Position below Name entry field
        # Bind focus-out event to Name entry for validation
        self.name_entry.bind("<FocusOut>", self.validate_name)
        # Gender radio buttons for Male/Female selection
        # lab_gender = Label(f_sign_in, text="Gender", bg='#B5B9F1', font=("Arial", 16))
        # lab_gender.place(x=160, y=300)

        radio_male = ctk.CTkRadioButton(f_sign_in, text="Male", variable=self.gender_var, value="Male")
        radio_male.place(x=180, y=305)
        radio_female = ctk.CTkRadioButton(f_sign_in, text="Female", variable=self.gender_var, value="Female")
        radio_female.place(x=350, y=305)

        # Submit button to complete the sign-in process
        btn_submit = ctk.CTkButton(f_sign_in, text=" Sign Up", fg_color='#A3A6F1',
                                    text_color='black', corner_radius=20,
                                    command=self.submit_registration, font=("Arial", 17))
        btn_submit.place(x=240, y=350)

    def create_input_field(self, frame, label_text, y_pos, show=None):
        """Helper function to create input fields for Name, Password, etc."""
        # label = Label(frame, text=label_text, bg='#B5B9F1', font=("Arial", 16))
        # label.place(x=50, y=y_pos)
        entry = ctk.CTkEntry(frame, width=300, height=35, corner_radius=10, border_width=1.5,
                             border_color="black", fg_color="white", text_color="black",
                             placeholder_text=f"{label_text}", show=show)
        entry.place(x=160, y=y_pos)
        return entry

    def checkname(self,name):
        for i in name:
            if not (i.isalpha() or i.isspace()):
                return False
        return True

    def validate_name(self, event):
        name = self.name_entry.get()
        if not self.checkname(name): 
            self.warning_label.config(text="Invalid!Use only letters.")
        else:
            self.warning_label.config(text="") 

    def checkage(self,age):
        try:
            age = int(age)  
            return 0 <= age <= 120 
        except ValueError:  
            return False
        
    def submit_registration(self):
        """Handle registration submission"""
        # Collect all input values
        name = self.name_entry.get()
        username = self.username_entry.get()
        age = self.age_entry.get()
        phone = self.phone_entry.get()
        password = self.password_entry.get()
        gender = self.gender_var.get()

        # Basic validation
        if not all([name, username, age, phone, password]):
            messagebox.showwarning("Registration Warning", "Please Fill All Fields")
            return

        if not name.replace(" ", "").isalpha():
            self.warning_label.config(text="Invalid name! Use only letters.", fg="red")
            return
        
        if not self.checkage(age):
            self.warning_label.config(text="Invalid Age! Enter a number between 0 and 120.")
            return
            
        self.warning_label.config(text="Registration Successful!", fg="green")

        self.insert_data_to_db(name, username, age, phone, gender, password)
        
        # Print user details
        print("Registration details:")
        print(f"Name: {name}")
        print(f"Username: {username}")
        print(f"Age: {age}")
        print(f"Phone: {phone}")
        print(f"Gender: {gender}")
        print("########")

        # Redirect to login or welcome page
        # self.app.show_frame('LogIn')

    def create_image_frame(self):
        """Create the frame that holds the image on the right side"""
        f4 = Frame(self.frame, width=500, height=400, bg='black') 
        f4.place(x=700, y=180)
        
        # Open and resize the image
        img = Image.open("Doctor.png").resize((500, 400))
        img = ImageTk.PhotoImage(img)
        
        img_label = Label(f4, image=img, bg='#B5B9F1')  
        img_label.place(x=0, y=0)
        img_label.image = img  # Keep a reference to the image to prevent garbage collection

    # def create_back_button(self):
    #     """Create the back button that navigates to the previous page"""
    #     btn1 = Button(self.frame, text="<back", font=("IM FELL Double Pica", 15, "bold"), 
    #                   fg="SteelBlue", bg="#B5B9F1", borderwidth=0,
    #                   command=lambda: self.app.show_frame('LogIn'))
    #     btn1.place(x=1125, y=10)

# Commented out main block for standalone testing
# if __name__ == "__main__":
#     root = Tk()
#     root.geometry('1200x750+150+25')
#     root.title('Sign Up Page')
#     root.resizable(False, False)
#     
#     # Create a dummy app class for testing
#     class DummyApp:
#         def show_frame(self, page_name):
#             print(f"Navigating to {page_name}")
#     
#     app = DummyApp()
#     signup_page = SignUp(root, app)
#     root.mainloop()