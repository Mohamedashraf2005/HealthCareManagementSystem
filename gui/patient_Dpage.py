import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image
import os
import sqlite3

#if you want connect with database write inside connect (db_path) مهم مهم مهم مهم مهم 
db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'HCMSclinic.db')

class PatientPage:
    def __init__(self, container, app):
        # self.frame = frame
        # self.frame.geometry('1200x750+150+25')
        # self.frame.title('Patient page')
        # self.frame.resizable(False, False)
        # self.frame.config(background='#B5B9F1')
        # self.frame.iconbitmap(r'C:\Users\lOl\Documents\GitHub\HealthCareManagementSystem\gui\PHOTO\logoIcon.ico')
        self.frame = Frame(container, width=1200, height=750, bg="#B5B9F1")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.app = app
        self.logo_image()
        self.create_frames()
        self.create_widgets()
        self.fetch_and_display_data()

    def logo_image(self):
        image = Image.open("logo.png").resize((110, 100)).convert("RGBA")
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

    def create_frames(self):
        # Frame of logout
        self.f1 = Frame(self.frame, width=1100, height=50, bg='#B5B9F1')
        self.f1.place(x=150, y=25)

        # Frame of welcome
        self.f2 = Frame(self.frame, width=1200, height=60, bg='#B5B9F1')
        self.f2.place(x=0, y=130)

        # Main frame of appointment request
        self.f3 = ctk.CTkFrame(self.frame, width=745, height=350, corner_radius=20, fg_color='white')
        self.f3.place(x=50, y=230)

        # Frame of patient info
        self.f6 = ctk.CTkFrame(self.frame, width=300, height=210, corner_radius=20, fg_color='white')
        self.f6.place(x=870, y=230)

    def create_widgets(self):
        # Logout button
        self.logout_button = ctk.CTkButton(
            self.f1, text='Log Out', fg_color='#336EA6', text_color='white',
            border_width=2, border_color='#336EA6', corner_radius=20, hover_color='#B5B9F1'
        )
        self.logout_button.place(x=850, y=12)

        # Welcome label
        self.welcome_label = ctk.CTkLabel(
            self.f2, text='Welcome,############', text_color='black',
            font=('Adobe Garamond Pro', 30, 'bold')
        )
        self.welcome_label.place(x=400, y=0)

        # Appointment requests label
        self.appointment_label = Label(
            self.f3, text='Appointment requests', fg='black', bg='white',
            font=("Felix Titling", 18, 'bold')
        )
        self.appointment_label.place(x=10, y=10)

        # Scrollable frame for appointments
        self.f5 = ctk.CTkScrollableFrame(self.f3, width=710, height=260, corner_radius=10)
        self.f5.place(x=5, y=55)

        # Patient info labels
        self.info_label = ctk.CTkLabel(self.f6, text='Patient INFO', text_color='black', font=('Felix Titling', 20))
        self.info_label.place(x=70, y=20)

        self.name_label = ctk.CTkLabel(self.f6, text='Name :', text_color='black', font=('Felix Titling', 20))
        self.name_label.place(x=15, y=60)

        self.age_label = ctk.CTkLabel(self.f6, text='Age :', text_color='black', font=('Felix Titling', 20))
        self.age_label.place(x=15, y=100)

        self.gender_label = ctk.CTkLabel(self.f6, text='Gender :', text_color='black', font=('Felix Titling', 20))
        self.gender_label.place(x=15, y=140)

        self.booked_label = ctk.CTkLabel(self.f6, text='Booked :', text_color='black', font=('Felix Titling', 20))
        self.booked_label.place(x=15, y=180)

        # Patient image
        self.img = Image.open(r"C:\Users\Anas\OneDrive\Desktop\HCMS\gui\PHOTO\fepatient.png").resize((300, 300))
        self.img = ImageTk.PhotoImage(self.img)
        self.img_label = Label(self.frame, image=self.img, bg='#B5B9F1')
        self.img_label.place(x=870, y=440)

        # Confirmation button
        self.confirm_button = ctk.CTkButton(
            self.frame, text='Confirmation', text_color='white', fg_color='#7579B9',
            corner_radius=20, hover_color='#B5B9F1', font=('arial', 20),
            border_width=2, border_color='#7579B9'
        )
        self.confirm_button.place(x=350, y=600)

    def fetch_and_display_data(self):
        # Fetch data from database
        conn = sqlite3.connect(db_path)
        cursor = conn.execute("""
            SELECT name, specialization, SessionfeeEGP, availabilityone, availabilitytwo, rating
            FROM doctor;
        """)
        data = cursor.fetchall()
        conn.close()

        # Columns headers
        columns = ["Name", "Category", "Fee", "Time 1", "Time 2", "Rating"]

        # Create headers
        for col_index, col_name in enumerate(columns):
            ctk.CTkLabel(self.f5, text=col_name, font=('Arial', 14, 'bold'), text_color='black').grid(row=0, column=col_index, padx=5, pady=2)

        # Populate data
        for row_index, row in enumerate(data, start=1):
            for col_index, value in enumerate(row):
                ctk.CTkLabel(self.f5, text=str(value), font=('arial', 12), text_color='black').grid(row=row_index, column=col_index, padx=5, pady=2)

            # Radio buttons
            radio_var = ctk.StringVar(value='other')
            ctk.CTkRadioButton(self.f5, text='Yes', value='yes', variable=radio_var, fg_color='green', hover_color='green').grid(row=row_index, column=len(columns), padx=2, pady=2)
            ctk.CTkRadioButton(self.f5, text='No', value='no', variable=radio_var, fg_color='red', hover_color='red').grid(row=row_index, column=len(columns) + 1, padx=2, pady=2)

# Run the application
if __name__ == "__main__":
    frame = Tk()
    app = PatientPage(frame)
    frame.mainloop()
