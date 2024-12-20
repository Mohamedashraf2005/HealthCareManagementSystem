import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image
import os
import sqlite3

#if you want connect with database write inside connect (db_path) مهم مهم مهم مهم مهم 
db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'HCMSclinic.db')

def get_resource_path(*path_parts):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, *path_parts)

class DoctorPage:
    def __init__(self, container, app):
        # self.frame = frame
        # self.frame.geometry('1200x750+150+25')
        # self.frame.title('Patient page')
        # self.frame.resizable(False, False)
        # self.frame.config(background='#B5B9F1')
        self.frame = Frame(container, width=1200, height=750, bg="#B5B9F1")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.app = app
        self.logo_image()
        self.create_frames()
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
        label.place(x=-6, y=0)
        return label

    def create_frames(self):
        # Frame for Logout
        self.f1 = Frame(self.frame, width=1100, height=50, bg='#B5B9F1')
        self.f1.place(x=120, y=25)

        # Frame for Welcome message
        self.f2 = Frame(self.frame, width=1200, height=60, bg='#B5B9F1')
        self.f2.place(x= 80, y=100)

        # Frame for Appointment Requests
        self.f3 = ctk.CTkFrame(self.frame, width=692, height=350, corner_radius=20, fg_color='white')
        self.f3.place(x=20, y=200)

        # Frame for Doctor Info
        self.f6 = ctk.CTkFrame(self.frame, width=250, height=100, corner_radius=20, fg_color='white')
        self.f6.place(x=830, y=250)

        # Frame for Rating
        self.f7 = ctk.CTkFrame(self.frame, width=250, height=100, corner_radius=20, fg_color='white')
        self.f7.place(x=830, y=380)

    def create_widgets(self):
        # Logout Button
        self.logout_button = ctk.CTkButton(
            self.f1, text='Log Out', fg_color='#336EA6', text_color='white',
            border_width=2, border_color='#336EA6', corner_radius=20, hover_color='#B5B9F1'
        )
        self.logout_button.place(x=850, y=12)

        # Welcome Label
        self.welcome_label = ctk.CTkLabel(
            self.f2, text='Welcome, Dr: #########', text_color='black',
            font=('Adobe Garamond Pro', 25, 'bold')
        )
        self.welcome_label.place(x=300, y=10)

        # Appointment Requests Label
        self.appointment_label = Label(
            self.f3, text='Appointment requests', fg='black', bg='white',
            font=("Felix Titling", 20, 'bold')
        )
        self.appointment_label.place(x=20, y=10)

        # Scrollable Frame for Appointment Requests
        self.f5 = ctk.CTkScrollableFrame(
            self.f3, width=658, height=220,
            label_text='Name \t\tGender \t\tAge \t\tTime  \t\tDone',
            corner_radius=10
        )
        self.f5.place(x=5, y=55)

        # Example content in the scrollable frame
        ctk.CTkLabel(self.f5, text='Label Example', font=('arial', 15)).grid(column=1, row=1)
        radio_var = ctk.StringVar(value='other')
        ctk.CTkRadioButton(self.f5, text='Yes', value='yes', variable=radio_var, fg_color='green', hover_color='green').grid(row=1, column=199)

        # Doctor Info Labels
        self.name_label = ctk.CTkLabel(self.f6, text='DR :', text_color='black', font=('Felix Titling', 20))
        self.name_label.place(x=15, y=20)

        self.age_label = ctk.CTkLabel(self.f6, text='Age :', text_color='black', font=('Felix Titling', 20))
        self.age_label.place(x=15, y=60)

        # Rating Frame Label
        self.rating_label = ctk.CTkLabel(self.f7, text='RATING', text_color='black', font=('Felix Titling', 20))
        self.rating_label.place(x=80, y=20)

        # Confirmation Button
        self.confirm_button = ctk.CTkButton(
            self.frame, text='Confirmation', text_color='white', fg_color='#7579B9',
            corner_radius=20, hover_color='#B5B9F1', font=('arial', 20),
            border_width=2, border_color='#7579B9'
        )
        self.confirm_button.place(x=700, y=580)

# Run the application
# if __name__ == "__main__":
#     frame = Tk()
#     app = PatientPage(frame)
#     frame.mainloop()

