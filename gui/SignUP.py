import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image

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
        
        # Initialize UI components
        self.logo_image()
        self.create_sign_in_frame()
        self.create_image_frame()
        # self.create_back_button()
    
    def logo_image(self):
        """Add the logo at the top of the window"""
        image = Image.open("logo.png").resize((150, 100))  # Resize the logo
        image = ImageTk.PhotoImage(image)  # Convert image to Tkinter format
        label = Label(self.frame, text="DocHub", compound="top", image=image, borderwidth=0, 
                      font=("IM FELL Double Pica", 15, "bold"), bg="#B5B9F1")
        label.image = image  # Keep a reference to the image
        label.place(x=10, y=0)  # Position the label
        return label

    def create_sign_in_frame(self):
        """Create the sign-in form with input fields and buttons"""
        f_sign_in = Frame(self.frame, width=600, height=500, bg='#B5B9F1')  
        f_sign_in.place(x=0, y=200)
        
        lab_sign_in_title = ctk.CTkLabel(f_sign_in, text="Sign Up", fg_color='#B5B9F1', 
                                          text_color='black', font=('Helvetica', 28))
        lab_sign_in_title.place(x=250, y=0)
        
        # Create input fields for each user detail
        self.name_entry = self.create_input_field(f_sign_in, "Name:", 50)
        self.password_entry = self.create_input_field(f_sign_in, "Password:", 250, show="*")
        self.username_entry = self.create_input_field(f_sign_in, "Username:", 100)
        self.age_entry = self.create_input_field(f_sign_in, "Age:", 150)
        self.phone_entry = self.create_input_field(f_sign_in, "Phone:", 200)

        # Gender radio buttons for Male/Female selection
        lab_gender = Label(f_sign_in, text="Gender:", bg='#B5B9F1', font=("Arial", 16))  
        lab_gender.place(x=50, y=300)
        
        radio_male = ctk.CTkRadioButton(f_sign_in, text="Male", variable=self.gender_var, value="Male")
        radio_male.place(x=160, y=305)
        radio_female = ctk.CTkRadioButton(f_sign_in, text="Female", variable=self.gender_var, value="Female")
        radio_female.place(x=230, y=305)

        # Submit button to complete the sign-in process
        btn_submit = ctk.CTkButton(f_sign_in, text="SIGN UP", fg_color='#A3A6F1', 
                                    text_color='black', corner_radius=20,
                                    command=self.submit_registration)
        btn_submit.place(x=250, y=350)

    def create_input_field(self, frame, label_text, y_pos, show=None):
        """Helper function to create input fields for Name, Password, etc."""
        label = Label(frame, text=label_text, bg='#B5B9F1', font=("Arial", 16))  
        label.place(x=50, y=y_pos)
        entry = ctk.CTkEntry(frame, width=300, height=35, corner_radius=10, border_width=2, 
                             border_color="black", fg_color="white", text_color="black", 
                             placeholder_text=f"Enter your {label_text.lower()}", show=show)
        entry.place(x=160, y=y_pos)
        return entry

    def submit_registration(self):
        """Handle registration submission"""
        # Collect all input values
        name = self.name_entry.get()
        password = self.password_entry.get()
        username = self.username_entry.get()
        age = self.age_entry.get()
        phone = self.phone_entry.get()
        gender = self.gender_var.get()

        # Basic validation
        if not all([name, password, username, age, phone]):
            # You might want to show an error message
            print("Please fill in all fields")
            return

        # Here you would typically:
        # 1. Validate inputs
        # 2. Check if username already exists
        # 3. Hash the password
        # 4. Save to database
        print("Registration details:")
        print(f"Name: {name}")
        print(f"Username: {username}")
        print(f"Age: {age}")
        print(f"Phone: {phone}")
        print(f"Gender: {gender}")

        # Redirect to login or welcome page
        self.app.show_frame('LogIn')

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