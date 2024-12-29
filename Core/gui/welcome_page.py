import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image
from SignIN import LogIn
from SignUP import SignUp
from AboutUS import About_Us
import os

def get_resource_path(*path_parts):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, *path_parts)
class WelcomePage:
    def __init__(self, container, app):
        self.frame = Frame(container, width=1200, height=750, bg='#B5B9F1')
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.app = app
        self.frame.config(background='#B5B9F1')
        self.logo_image()
        self.create_widgets()
        
        # Store reference to the main application
        self.app = app

        # Configure frame
        self.frame.config(background='#B5B9F1')

        self.logo_image()
        self.create_widgets()

   
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

    def create_widgets(self):
        f1 = Frame(self.frame, width=1200, height=70, bg='#B5B9F1')  
        f1.place(x=150, y=17)

        btn1 = ctk.CTkButton(f1, text='Home', fg_color='#B5B9F1', text_color='black', 
                              border_width=2, border_color="black", corner_radius=20, 
                              hover_color='#A3A6F1')
        btn1.place(x=15, y=20)

        btn2 = ctk.CTkButton(f1, text='About us', fg_color='#B5B9F1', text_color='black', 
                              border_width=2, border_color="black", corner_radius=20, 
                              hover_color='#A3A6F1',
                             command=lambda: self.app.show_frame(About_Us))
        btn2.place(x=165, y=20)

      

        # Add navigation to SignUp page
        btn5 = ctk.CTkButton(f1, text='Sign up', fg_color='black', text_color='white', 
                              border_width=2, border_color="black", corner_radius=20, 
                              hover_color='#A3A6F1',
                              command=lambda: self.app.show_frame(SignUp))
        btn5.place(x=700, y=20)

        # Add navigation to LogIn page
        btn6 = ctk.CTkButton(f1, text='Log in', fg_color='#B5B9F1', text_color='black', 
                              border_width=2, border_color="black", corner_radius=20, 
                              hover_color='#A3A6F1',
                              command=lambda: self.app.show_frame(LogIn))
        btn6.place(x=850, y=20)

        f2 = Frame(self.frame, width=1600, height=100, bg='#B5B9F1')  
        f2.place(x=1, y=150)

        lab1 = ctk.CTkLabel(f2, text='Welcome', fg_color='black', text_color='white', 
                             font=('Helvetica', 33), corner_radius=15)
        lab1.place(x=510, y=40)

        f3 = Frame(self.frame, width=800, height=500, bg='#B5B9F1') 
        f3.place(x=20, y=250)

        lab2 = Label(f3, text='Healing Elevation', fg='red', bg='#B5B9F1', font=("Arial", 35))  
        lab2.place(x=20, y=100)

        lab3 = Label(f3, text='Revitalize Your Health', fg='white', bg='#B5B9F1', font=("Arial", 35))  
        lab3.place(x=20, y=155)

        lab4 = Label(f3, text='Book your appointment now ..', fg='black', bg='white', 
                     width=27, height=2, font=('Arial', 15))  
        lab4.place(x=100, y=290)

        f4 = Frame(self.frame, width=400, height=400, bg='#B5B9F1') 
        f4.place(x=730, y=250)

        self.display_image(f4) 

    def display_image(self, frame):
        img = Image.open(get_resource_path("PHOTO", "welcome.png")).resize((465, 500))
        img = ImageTk.PhotoImage(img) 
        img_label = Label(frame, image=img, bg='#B5B9F1') 
        img_label.image = img  
        img_label.pack()



# Commented out the main block as this will now be used in a multi-page application
# If you want to test it standalone, you can uncomment and modify:
# if __name__ == "__main__":
#     root = Tk()
#     root.geometry('1200x750+150+25')
#     root.title('Welcome Page')
#     root.resizable(False, False)
#     
#     # Create a dummy app class for testing
#     class DummyApp:
#         def show_frame(self, page_name):
#             print(f"Navigating to {page_name}")
#     
#     app = DummyApp()
#     welcome_page = WelcomePage(root, app)
#     root.mainloop()