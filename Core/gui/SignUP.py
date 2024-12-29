from tkinter import messagebox
import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image
import os
import sqlite3
from idpatientlist import idlistpatient

#if you want connect with database write inside connect (db_path) مهم مهم مهم مهم مهم 
db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'HCMSclinic.db')

def get_resource_path(*path_parts):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, *path_parts)
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
    def create_sign_in_frame(self):
        """Create the sign-in form with input fields and buttons."""
        f_sign_in = Frame(self.frame, width=600, height=500, bg='#B5B9F1')
        f_sign_in.place(x=200, y=200) 
        lab_sign_in_title = ctk.CTkLabel(f_sign_in, text="Create Account", fg_color='#B5B9F1',
                                         text_color='black', font=('Helvetica', 28))
        lab_sign_in_title.place(x=205, y=0)
        # Create input fields for each user detail
        self.name_entry = self.create_input_field(f_sign_in, "Name", 50)
        self.username_entry = self.create_input_field(f_sign_in, "Username", 100)
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

    def checkname(self, name):
        """Validate that the name contains only letters and spaces."""
        return all(i.isalpha() or i.isspace() for i in name)

    def validate_name(self, event):
        name = self.name_entry.get()
        if not self.checkname(name): 
            self.warning_label.config(text="Invalid! Use only letters.")
        else:
            self.warning_label.config(text="") 

    def checkage(self, age):
        """Validate that the age is a valid integer between 0 and 120."""
        try:
            age = int(age)  
            return 0 <= age <= 120 
        except ValueError:  
            return False
    def insert_patient(self, name, username, password, age, gender, phone):
        """Insert patient details into the database."""
        conn = sqlite3.connect(db_path)

        cursor = conn.cursor()

        insert_query = """
        INSERT INTO patient (name, username, password, age, gender, phone)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            cursor.execute(insert_query, (name, username, password, (age), gender, phone))
            conn.commit()
            messagebox.showinfo("Success", "Registration Successful!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
        finally:
            conn.close()
    def submit_registration(self):
        """Handle registration submission."""
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

        if not self.checkname(name):
            self.warning_label.config(text="Invalid name! Use only letters.", fg="red")
            return

        if not self.checkage(age):
            messagebox.showerror("Invalid Input", "Age must be a number between 0 and 120.")
            return
     
    # self.warning_label.config(text="Registration Successful!", fg="green")

        # Insert patient into database
        self.insert_patient(name, username, password, age, gender, phone)

    def create_image_frame(self):
        """Create the frame that holds the image on the right side."""
        f4 = Frame(self.frame, width=500, height=400, bg='black') 
        f4.place(x=700, y=180)
       
        img = Image.open(get_resource_path("PHOTO", "Doctor.png")).resize((500, 400))
        img = ImageTk.PhotoImage(img)
        img_label = Label(f4, image=img, bg='#B5B9F1')  
        img_label.place(x=0, y=0)
        img_label.image = img  # Keep a reference to the image

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
