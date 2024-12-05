import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image

class SignUp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x750+150+25')
        self.root.title('Log In')
        self.root.resizable(False, False)
        self.root.config(background='#B5B9F1')
        
        self.logo_image()
        self.create_sign_in_frame()
        self.create_image_frame()
        self.create_back_button()
    
    def logo_image(self):
        """Add the logo at the top of the window"""
        image = Image.open("logo.png").resize((150, 100))  # Resize the logo
        image = ImageTk.PhotoImage(image)  # Convert image to Tkinter format
        label = Label(self.root, text="DocHub", compound="top", image=image, borderwidth=0, 
                      font=("IM FELL Double Pica", 15, "bold"), bg="#B5B9F1")
        label.image = image  # Keep a reference to the image
        label.place(x=10, y=0)  # Position the label
        return label

    def create_sign_in_frame(self):
        """Create the sign-in form with input fields and buttons"""
        f_sign_in = Frame(self.root, width=600, height=500, bg='#B5B9F1')  
        f_sign_in.place(x=0, y=200)
        
        lab_sign_in_title = ctk.CTkLabel(f_sign_in, text="Sign Up", fg_color='#B5B9F1', text_color='black', font=('Helvetica', 28))
        lab_sign_in_title.place(x=250, y=0)
        
        # Create input fields for each user detail
        self.create_input_field(f_sign_in, "Name:", 50)
        self.create_input_field(f_sign_in, "Password:", 100, show="*")
        self.create_input_field(f_sign_in, "UserName:", 150)
        self.create_input_field(f_sign_in, "Age:", 200)
        self.create_input_field(f_sign_in, "Phone:", 250)

        # Gender radio buttons for Male/Female selection
        lab_gender = Label(f_sign_in, text="Gender:", bg='#B5B9F1', font=("Arial", 16))  
        lab_gender.place(x=50, y=300)
        gender_var = StringVar(value="Male")  # Default value is Male
        radio_male = ctk.CTkRadioButton(f_sign_in, text="Male", variable=gender_var, value="Male")
        radio_male.place(x=160, y=305)
        radio_female = ctk.CTkRadioButton(f_sign_in, text="Female", variable=gender_var, value="Female")
        radio_female.place(x=230, y=305)

        # Submit button to complete the sign-in process
        btn_submit = ctk.CTkButton(f_sign_in, text="SIGN IN", fg_color='#A3A6F1', text_color='black', corner_radius=20)
        btn_submit.place(x=250, y=350)

    def create_input_field(self, frame, label_text, y_pos, show=None):
        """Helper function to create input fields for Name, Password, etc."""
        label = Label(frame, text=label_text, bg='#B5B9F1', font=("Arial", 16))  
        label.place(x=50, y=y_pos)
        entry = ctk.CTkEntry(frame, width=300, height=35, corner_radius=10, border_width=2, 
                             border_color="black", fg_color="white", text_color="black", 
                             placeholder_text=f"Enter your {label_text.lower()}", show=show)
        entry.place(x=160, y=y_pos)

    def create_image_frame(self):
        """Create the frame that holds the image on the right side"""
        f4 = Frame(self.root, width=500, height=400, bg='black') 
        f4.place(x=700, y=180)
        
        # Open and resize the image
        img = Image.open("D:/Project/Python Folder/Doctor.png").resize((500, 400))
        img = ImageTk.PhotoImage(img)
        
        img_label = Label(f4, image=img, bg='#B5B9F1')  
        img_label.place(x=0, y=0)
        img_label.image = img  # Keep a reference to the image to prevent garbage collection

    def create_back_button(self):
        """Create the back button that navigates to the previous page"""
        btn1 = Button(self.root, text="<back", font=("IM FELL Double Pica", 15, "bold"), 
                      fg="SteelBlue", bg="#B5B9F1", borderwidth=0)
        btn1.place(x=1125, y=10)

if __name__ == "__main__":
    root = Tk()
    sign_up_page = SignUp(root)
    root.mainloop()
