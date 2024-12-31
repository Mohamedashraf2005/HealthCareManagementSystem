import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image
import os

def get_resource_path(*path_parts):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, *path_parts)

class About_Us:
    def __init__(self, container, app):
        # Create the frame as a child of the container
        self.frame = Frame(container, width=1200, height=750, bg='#B5B9F1')
        self.frame.grid(row=0, column=0, sticky="nsew")  # Use grid layout for flexibility

        self.app = app  # You can use 'app' for managing application-wide settings

        # Initialize components
        self.logo_image()
        self.create_widgets()

        # Variables to manage positioning of sections
        self.male_y = 250
        self.female_y = 350

        # Add male and female sections
        self.Male_Section("Anas Elgezawy", "anaselgezawy@gmail.com")
        self.Male_Section("Ali Elbahrawy", "ali.fathy.ali20@gmail.com")
        self.Male_Section("Mohamed Ahmed", "mohmedahmedali159@gmail.com")
        self.Male_Section("Mohamed Ashraf", "mohamedachrvf@gmail.com")
        self.Female_Section("Eman Hekal", "hekaleman103@gmail.com")
        self.Female_Section("Mariam Ahmed", "mariamsalama369@gmail.com")

    def logo_image(self):
        image = Image.open(get_resource_path("PHOTO", "logo.png")).resize((150, 100)).convert("RGBA")
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

    def create_widgets(self):
        f2 = Frame(self.frame, width=900, height=100, bg='#B5B9F1')  
        f2.place(x=1, y=120)

        lab1 = ctk.CTkLabel(f2, text='About US', fg_color='black', text_color='white', font=('Times new roman', 33), corner_radius=15)
        lab1.place(x=510, y=15)

        # Add the new title under "About Us"
        about_text = "We’re AI students Batch 2027 \nThis project is all about our teamwork and dedication,\nWe proudly presented 29th December 2024!"
        lab2 = ctk.CTkLabel(self.frame, text=about_text, fg_color='black', text_color='white', font=('Times new roman', 20), corner_radius=15)
        lab2.place(x=380, y=180)  # Adjust the position as needed

    def Male_Section(self, name, Email):
        male_icon = Image.open(get_resource_path("PHOTO", "ManIco.png")).resize((50, 50)).convert("RGBA")
        male_icon = ImageTk.PhotoImage(male_icon)
        male_label = Label(self.frame, image=male_icon, compound="left",
                           text=f"  {name} \n  {Email}",
                           font=("Times new roman", 15), bg="#B5B9F1", fg="black")
        male_label.image = male_icon
        male_label.place(x=150, y=self.male_y)  
        self.male_y += 100  

    def Female_Section(self, name, Email):
        female_icon = Image.open(get_resource_path("PHOTO", "FemaleIco.png")).resize((50, 50)).convert("RGBA")
        female_icon = ImageTk.PhotoImage(female_icon)
        female_label = Label(self.frame, image=female_icon, compound="left",
                            text=f"  {name} \n  {Email}",
                            font=("Times new roman", 15), bg="#B5B9F1", fg="black")
        female_label.image = female_icon
        female_label.place(x=750, y=self.female_y)  
        self.female_y += 100  

        self.logout_button = ctk.CTkButton(
                self.frame, text='Close', fg_color='#336EA6', text_color='white',
                border_width=2, border_color='#336EA6', corner_radius=20, hover_color='#B5B9F1',command=self.app.root.destroy
            )
        self.logout_button.place(x=1000, y=25)