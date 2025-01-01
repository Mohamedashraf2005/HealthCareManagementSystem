import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image
import os
import sqlite3
from tkinter import messagebox
import dbfunctions as dbf

#if you want connect with database write inside connect (db_path) مهم مهم مهم مهم مهم 
db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'HCMSclinic.db')

def get_resource_path(*path_parts):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, *path_parts)

class DoctorPage:
    def __init__(self, container, app):
        print("\nDEBUG  doctor HEREEEEE######\n")
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
        self.f3.place(x=80, y=200)

        # Frame for Doctor Info
        # self.f6 = ctk.CTkFrame(self.frame, width=250, height=100, corner_radius=20, fg_color='white')
        # self.f6.place(x=830, y=250)

        # # Frame for Rating
        # self.f7 = ctk.CTkFrame(self.frame, width=250, height=100, corner_radius=20, fg_color='white')
        # self.f7.place(x=830, y=380)

        self.f354 = ctk.CTkFrame(self.frame, width=160, height=80, corner_radius=20, fg_color='white')
        self.f354.place(x=930, y=100)

    def create_widgets(self):
        self.OTP_entry = self.create_input_field(self.f354, "Enter OTP", 10)

        btn_submit = ctk.CTkButton(self.f354, text="Confirm", fg_color='#3971a9',
                                   text_color='white', corner_radius=20,
                                   command=self.submit_otp, font=("Arial", 17))
        btn_submit.place(x=9, y=50)
        # Logout Button
        self.logout_button = ctk.CTkButton(
            self.f1, text='Log Out', fg_color='#336EA6', text_color='white',
            border_width=2, border_color='#336EA6', corner_radius=20, hover_color='#B5B9F1',command=self.app.root.destroy
        )
        self.logout_button.place(x=850, y=12)

        # Welcome Label
        # self.welcome_label = ctk.CTkLabel(
        #     self.f2, text='Welcome, Dr: #########', text_color='black',
        #     font=('Adobe Garamond Pro', 25, 'bold')
        # )
        # self.welcome_label.place(x=300, y=10)

        # Appointment Requests Label
        self.appointment_label = Label(
            self.f3, text='Appointment requests', fg='black', bg='white',
            font=("Felix Titling", 20, 'bold')
        )
        self.appointment_label.place(x=20, y=10)

        # Scrollable Frame for Appointment Requests
        self.f5 = ctk.CTkScrollableFrame(
            self.f3, width=658, height=220,
            label_text='Name \t\tAge \t\tGender \t\tPhone  \t\tDone',
            corner_radius=10
        )
        self.f5.place(x=5, y=55)

        # Example content in the scrollable frame
        ctk.CTkLabel(self.f5, text='\tYou have No UpComing Appointements!', font=('arial', 25)).grid(column=1, row=1)
        # radio_var = ctk.StringVar(value='other')
        # ctk.CTkRadioButton(self.f5, text='Yes', value='yes', variable=radio_var, fg_color='green', hover_color='green').grid(row=1, column=199)


    def submit_otp(self):
        if self.OTP_entry is None or self.OTP_entry.get() == "":
            print("ERROR: OTP entry is None or empty!")
        else:
            otp_value = self.OTP_entry.get()
            print(f"OTP Value: {otp_value}")

            # Call OTPVerify function to validate the OTP
            if dbf.OTPVerifydoctor(otp_value):
                doctor_id = otp_value  # Assuming OTP value is the doctor's ID
                self.display_assigned_patients(doctor_id)
                # messagebox.showinfo("Success", "OTP Verified Successfully!")
                
                conn = sqlite3.connect(db_path)
                cursor = conn.execute("""
                    SELECT name, age, rating, username
                    FROM doctor
                    WHERE id = ?;
                """, (otp_value,))
                datadoctor = cursor.fetchall()
                conn.close()


                if datadoctor:
                    first_doctor_name = datadoctor[0][0]

                    # Check if the name already starts with 'Dr ' and handle accordingly
                    if first_doctor_name.startswith("Dr "):
                        display_name = first_doctor_name  # Use as is
                    else:
                        display_name = f"Dr {first_doctor_name}"  # Add 'Dr ' prefix

                    # Create the Welcome label
                    self.welcome_label = ctk.CTkLabel(
                        self.f2,
                        text=f'Welcome, {display_name},',
                        text_color='black',
                        font=('Adobe Garamond Pro', 30, 'bold')
                    )
                    self.welcome_label.place(x=310, y=10)

                    # Call the function to display the welcome message
                    self.show_welcome_message(display_name)
                    # Initialize y-coordinate for label placement
                    y_offset = 60

                    # Loop through the patient data and display it
                    for doctor in datadoctor:
                        name, age, rating, username = doctor
                       
                        self.f6 = ctk.CTkFrame(self.frame, width=275, height=100, corner_radius=20, fg_color='white')
                        self.f6.place(x=830, y=250)

                        # Frame for Rating
                        self.f7 = ctk.CTkFrame(self.frame, width=250, height=70, corner_radius=20, fg_color='white')
                        self.f7.place(x=830, y=380)

                        username_label = ctk.CTkLabel(self.f6, text=f'Username: {username}', text_color='black', font=('Felix Titling', 20))
                        username_label.place(x=15, y=y_offset + 160)
                        self.name_label = ctk.CTkLabel(self.f6, text=f'DR : {name}', text_color='black', font=('Felix Titling', 20))
                        self.name_label.place(x=15, y=20)

                        self.age_label = ctk.CTkLabel(self.f6, text=f'Age : {age}', text_color='black', font=('Felix Titling', 20))
                        self.age_label.place(x=15, y=60)

                        self.rating_label = ctk.CTkLabel(self.f7, text=f'RATING : {rating}', text_color='black', font=('Felix Titling', 20))
                        self.rating_label.place(x=50, y=20)

                        # Update y_offset to separate records visually
                        y_offset += 200

                    # Destroy the f355 frame
                    if self.f354:
                        self.f356 = ctk.CTkFrame(self.frame, width=160, height=80, corner_radius=20, fg_color='#b5b9f1')
                        self.f356.place(x=930, y=100)
                        print("f354 frame has been removed.")
            else:
                # If OTP is invalid, show an error message
                print("Invalid OTP!")
                messagebox.showerror("Error", "Invalid OTP, please try again.")

    def show_welcome_message(self, first_doctor_name):
        welcome_text = f"Welcome, {first_doctor_name}"
        self.update_label(welcome_text, 0)

    def update_label(self, welcome_text, index):
        # Update the label text one character at a time
        if index < len(welcome_text):
            current_text = welcome_text[:index + 1]
            self.welcome_label.configure(text=current_text)
            # Call update_label again after 100ms
            self.f2.after(50, self.update_label, welcome_text, index + 1)  # هنا استخدم self.f2

    def create_input_field(self, frame, label_text, y_pos, show=None):
        entry = ctk.CTkEntry(frame, width=150, height=35, corner_radius=10, border_width=1.5,
                             border_color="black", fg_color="white", text_color="black",
                             placeholder_text=f"{label_text}", show=show)
        entry.place(x=5, y=y_pos)
        return entry


    def display_assigned_patients(self, doctor_id):
        """
        Fetch and display all patients assigned to the logged-in doctor.
        
        Args:
        doctor_id (str): ID of the logged-in doctor.
        """
        try:
            # Connect to the database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Step 1: Get patient usernames from the Appointment_clinic table
            cursor.execute("""
                SELECT patient_username
                FROM Appointment_clinc
                WHERE doctor_id = ?;
            """, (doctor_id,))
            patient_usernames = cursor.fetchall()

            # Flatten the list of tuples
            patient_usernames = [row[0] for row in patient_usernames]

            # Step 2: Get patient details from the patient table
            if patient_usernames:
                cursor.execute(f"""
                    SELECT name, age, gender, phone
                    FROM patient
                    WHERE username IN ({','.join(['?'] * len(patient_usernames))});
                """, patient_usernames)
                patient_data = cursor.fetchall()

                # Step 3: Populate the scrollable frame with patient details
                for widget in self.f5.winfo_children():
                    widget.destroy()  # Clear any previous data in the frame

                if patient_data:
                    for idx, (name, age, gender, phone ) in enumerate(patient_data, start=1):
                        patient_info = f"       {name}          {age}           {gender}        {phone}     "
                        ctk.CTkLabel(self.f5, text=patient_info, font=('Arial', 15), anchor="w").grid(row=idx, column=0, sticky="w")
                else:
                    # No patients found
                    ctk.CTkLabel(self.f5, text="No assigned patients.", font=('Arial', 15)).grid(row=0, column=0, sticky="w")
            else:
                # No patient usernames found
                ctk.CTkLabel(self.f5, text="No assigned patients.", font=('Arial', 15)).grid(row=0, column=0, sticky="w")

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            messagebox.showerror("Error", "Failed to retrieve patient data.")

        finally:
            if conn:
                conn.close()

# Run the application
# if __name__ == "__main__":
#     frame = Tk()
#     app = PatientPage(frame)
#     frame.mainloop()



