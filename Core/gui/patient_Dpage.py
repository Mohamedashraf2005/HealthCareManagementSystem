import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image
import os
import sqlite3
import dbfunctions as dbf
from tkinter import messagebox

db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'HCMSclinic.db')

def get_resource_path(*path_parts):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, *path_parts)

class PatientPage:
    def __init__(self, container, app):
        self.frame = Frame(container, width=1200, height=750, bg="#B5B9F1")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.app = app
        self.selected_doctor_username = None
        self.logo_image()
        self.create_frames()
        self.create_widgets()
        self.fetch_and_display_data()

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

    def create_frames(self):
        # Frame of logout
        self.f1 = Frame(self.frame, width=1100, height=50, bg='#B5B9F1')
        self.f1.place(x=150, y=25)

        # Frame of welcome
        self.f2 = Frame(self.frame, width=1200, height=60, bg='#B5B9F1')
        self.f2.place(x=0, y=130)

        # Main frame of appointment request
        self.f3 = ctk.CTkFrame(self.frame, width=745, height=350, corner_radius=20, fg_color='white')
        self.f3.place(x=20, y=230)

        self.f355 = ctk.CTkFrame(self.frame, width=160, height=80, corner_radius=20, fg_color='white')
        self.f355.place(x=930, y=100)

    def create_widgets(self):
        self.OTP_entry = self.create_input_field(self.f355, "Enter OTP", 10)

        btn_submit = ctk.CTkButton(self.f355, text="Confirm", fg_color='#3971a9',
                                   text_color='white', corner_radius=20,
                                   command=self.submit_otp, font=("Arial", 17))
        btn_submit.place(x=9, y=50)

        self.logout_button = ctk.CTkButton(
            self.f1, text='Log Out', fg_color='#336EA6', text_color='white',
            border_width=2, border_color='#336EA6', corner_radius=20, hover_color='#B5B9F1', command=self.app.root.destroy
        )
        self.logout_button.place(x=850, y=12)

        self.appointment_label = Label(
            self.f3, text='Appointment requests', fg='black', bg='white',
            font=("Felix Titling", 18, 'bold')
        )
        self.appointment_label.place(x=10, y=10)

        self.f5 = ctk.CTkScrollableFrame(self.f3, width=710, height=260, corner_radius=10)
        self.f5.place(x=5, y=55)

        self.confirm_button = ctk.CTkButton(
            self.frame, text='Confirmation', text_color='white', fg_color='#7579B9',
            corner_radius=20, hover_color='#B5B9F1', font=('arial', 20),
            border_width=2, border_color='#7579B9',
            command=self.confirm_appointment
        )
        self.confirm_button.place(x=350, y=620)

    def submit_otp(self):
        if self.OTP_entry is None or self.OTP_entry.get() == "":
            print("ERROR: OTP entry is None or empty!")
        else:
            otp_value = self.OTP_entry.get()
            print(f"OTP Value: {otp_value}")

            # Call OTPVerify function to validate the OTP
            if dbf.OTPVerify(otp_value):
                # If OTP is valid, proceed with further actions
                print("OTP is valid, proceeding with further actions...")
                
                with sqlite3.connect(db_path) as conn:
                    cursor = conn.execute("""
                        SELECT name, age, gender, username
                        FROM patient
                        WHERE id = ?;
                    """, (otp_value,))
                    datapatient = cursor.fetchall()
                    print(datapatient)

                if datapatient:
                    first_patient_name = datapatient[0][0]
                    usernamepatientpass=datapatient[0][3]

                    # Create the Welcome label
                    self.welcome_label = ctk.CTkLabel(
                        self.f2,
                        text=f'Welcome, {first_patient_name},',
                        text_color='black',
                        font=('Adobe Garamond Pro', 30, 'bold')
                    )
                    self.welcome_label.place(x=350, y=10)

                    # Call the function to display the welcome message
                    self.show_welcome_message(first_patient_name)
                    # Initialize y-coordinate for label placement
                    y_offset = 60

                    # Loop through the patient data and display it
                    for patient in datapatient:
                        name, age, gender, username = patient
                        booked = "Empty,Book Now!"  # Use None for the booked column
                        self.f6 = ctk.CTkFrame(self.frame, width=300, height=210, corner_radius=20, fg_color='white')
                        self.f6.place(x=870, y=230)
                        self.info_label = ctk.CTkLabel(self.f6, text='Patient INFO', text_color='black', font=('Felix Titling', 20))
                        self.info_label.place(x=70, y=20)
                        name_label = ctk.CTkLabel(self.f6, text=f'Name: {name}', text_color='black', font=('Felix Titling', 20))
                        name_label.place(x=15, y=y_offset)

                        age_label = ctk.CTkLabel(self.f6, text=f'Age: {age}', text_color='black', font=('Felix Titling', 20))
                        age_label.place(x=15, y=y_offset + 40)

                        gender_label = ctk.CTkLabel(self.f6, text=f'Gender: {gender}', text_color='black', font=('Felix Titling', 20))
                        gender_label.place(x=15, y=y_offset + 80)

                        booked_label = ctk.CTkLabel(self.f6, text=f'Booked: {booked}', text_color='black', font=('Felix Titling', 20))
                        booked_label.place(x=15, y=y_offset + 120)

                        username_label = ctk.CTkLabel(self.f6, text=f'Username: {username}', text_color='black', font=('Felix Titling', 20))
                        username_label.place(x=15, y=y_offset + 160)

                        # Update y_offset to separate records visually
                        y_offset += 200

                    # Destroy the f355 frame
                    if self.f355:
                        self.f356 = ctk.CTkFrame(self.frame, width=160, height=80, corner_radius=20, fg_color='#b5b9f1')
                        self.f356.place(x=930, y=100)
                        print("f355 frame has been removed.")
            else:
                # If OTP is invalid, show an error message
                print("Invalid OTP!")
                messagebox.showerror("Error", "Invalid OTP, please try again.")

    def show_welcome_message(self, first_patient_name):
        welcome_text = f"Welcome, {first_patient_name}"
        self.update_label(welcome_text, 0)

    def update_label(self, welcome_text, index):
        # Update the label text one character at a time
        if index < len(welcome_text):
            current_text = welcome_text[:index + 1]
            self.welcome_label.configure(text=current_text)
            # Call update_label again after 100ms
            self.f2.after(50, self.update_label, welcome_text, index + 1)

    def create_input_field(self, frame, label_text, y_pos, show=None):
        entry = ctk.CTkEntry(frame, width=150, height=35, corner_radius=10, border_width=1.5,
                             border_color="black", fg_color="white", text_color="black",
                             placeholder_text=f"{label_text}", show=show)
        entry.place(x=5, y=y_pos)
        return entry

    def fetch_and_display_data(self):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.execute("""
                SELECT username, name, specialization, SessionfeeEGP, availabilityone, availabilitytwo, rating
                FROM doctor;
            """)
            data = cursor.fetchall()

        columns = ["Name", "Category", "Fee", "Time 1", "Time 2", "Rating", "Select"]

        for col_index, col_name in enumerate(columns):
            ctk.CTkLabel(self.f5, text=col_name, font=('Arial', 14, 'bold'), text_color='black').grid(row=0, column=col_index, padx=5, pady=2)

        for row_index, row in enumerate(data, start=1):
            for col_index, value in enumerate(row[1:]):
                ctk.CTkLabel(self.f5, text=str(value), font=('arial', 12), text_color='black').grid(row=row_index, column=col_index, padx=5, pady=2)

            doctor_username = row[0]  # Assuming the last value is the doctor's username

            # Radio button for selecting a doctor
            radio_button = ctk.CTkRadioButton(
                self.f5, text='Yes', value=row[0],  # Ensure `row[-1]` is the doctor's username
                variable=self.selected_doctor_username,
                fg_color='green', hover_color='green',
                command=lambda username=row[0]: self.select_doctor(username)
            )
            radio_button.grid(row=row_index, column=len(columns) - 1, padx=2, pady=2)

    def select_doctor(self, doctor_username):
        if not hasattr(self, 'selected_doctors'):
            self.selected_doctors = []  # قائمة لتخزين أسماء الأطباء المختارين

        if doctor_username not in self.selected_doctors:
            self.selected_doctors.append(doctor_username)  # إضافة الطبيب إلى القائمة
            print(f"Doctor added: {doctor_username}")
        else:
            self.selected_doctors.remove(doctor_username)  # إزالة الطبيب من القائمة إذا كان موجودًا
            print(f"Doctor removed: {doctor_username}")

    def confirm_appointment(self):
        if not hasattr(self, 'selected_doctors') or not self.selected_doctors:
            messagebox.showerror("Error", "Please select at least one doctor.")
            return

        if not hasattr(self, 'OTP_entry') or self.OTP_entry is None:
            messagebox.showerror("Error", "OTP Entry widget is not initialized.")
            return

        otp_value = self.OTP_entry.get()
        if not otp_value:
            messagebox.showerror("Error", "Please enter your OTP.")
            return

        try:
            # Fetch patient username and details
            with sqlite3.connect(db_path) as conn:
                cursor = conn.execute("""
                    SELECT username, name
                    FROM patient
                    WHERE id = ?;
                """, (otp_value,))
                patient_data = cursor.fetchone()

            if not patient_data:
                messagebox.showerror("Error", "Invalid OTP. No patient found.")
                return

            patient_username, patient_name = patient_data

            # Record the appointments for all selected doctors
            with sqlite3.connect(db_path) as conn:
                for doctor_username in self.selected_doctors:
                    conn.execute("""
                        INSERT INTO Appointment_clinc (patient_username, doctor_username)
                        VALUES (?, ?);
                    """, (patient_username, doctor_username))
                conn.commit()

            messagebox.showinfo("Success", f"Appointments confirmed for {patient_name} with selected doctors.")
            print(f"Appointments successfully created for patient {patient_username} with doctors {self.selected_doctors}.")

            # Clear the list of selected doctors after confirmation
            self.selected_doctors.clear()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            print(f"Database error: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    frame = Tk()
    app = PatientPage(frame, None)
    frame.mainloop()