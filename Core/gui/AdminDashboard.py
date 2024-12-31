from tkinter import *
from tkinter import Label, Button, Entry, Frame, DISABLED, NORMAL
from tkinter import Frame, Entry, Label, StringVar, Radiobutton, ttk, Canvas, VERTICAL, RIGHT, Y, LEFT, BOTH, X, Button
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import os
import sqlite3
import time
from threading import Thread

#if you want connect with database write inside connect (db_path) مهم مهم مهم مهم مهم 
db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'HCMSclinic.db')

def get_resource_path(*path_parts):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, *path_parts)
class AdminDashboard:
    def __init__(self, container, app):

        self.frame = Frame(container, width=1200, height=750, bg="#B5B9F1")
        self.frame.grid(row=0, column=0, sticky="nsew")
        # self.frame.title("Admin Dashboard")
        # self.frame.resizable(False, False)
        ###
        self.master = app  # Reference to MainApplication
        self.app = app
        ###
        self.logo_image()
        self.add_logout_button()
        self.add_welcome_message()
        self.add_statistics_with_curves()
        self.add_buttons_with_curves()
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

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

    def add_logout_button(self):
        f1 = Frame(self.frame, width=1100, height=50, bg='#B5B9F1')
        f1.place(x=150, y=25)
        
        button1 = ctk.CTkButton(
            f1, 
            text='Log Out', 
            fg_color='#336EA6', 
            text_color='white', 
            border_width=2, 
            border_color='#336EA6', 
            corner_radius=20, 
            hover_color='#B5B9F1', 
            command=self.master.root.destroy
        )


        button1.place(x=850, y=12)


    def add_welcome_message(self):

        welcome_label = Label(self.frame, text="Welcome, Admin..", font=("Arial", 18, "bold"), bg="#B5B9F1", fg="#000")
        welcome_label.place(x=500, y=30)


    def add_statistics_with_curves(self):
        conn = sqlite3.connect(db_path)
        ptpatient = conn.execute("""
                        SELECT COUNT(*)
                        FROM patient;
                        """).fetchone()[0]
    
    # Count the number of rows in the doctor table
        ptdoctor = conn.execute("""
                        SELECT COUNT(*)
                        FROM doctor;
                        """).fetchone()[0]
        
        numberofpateints=ptpatient
        numberofdoctors=ptdoctor
        conn.commit()
        conn.close()
        stats = [
            ("Patients",numberofpateints),
            ("Doctors", numberofdoctors),
            ("Balance", "78,000$"),
        ]

        x_positions = [275, 530, 780]  
        for i, (text, value) in enumerate(stats):
            self.create_rounded_frame(x_positions[i], 80, 150, 80, text, value)#y-axis,w-frame,h-frame,text-frame

    def add_buttons_with_curves(self):
        buttons = [
            ("View Patients", self.view_patient),
            ("View Doc", self.view_doc),
            ("Add Doc", self.add_doc),
            ("Update Doc", self.update_doc),
            ("Remove Doc", self.remove_doc),
        ]

        x_positions = [190,360, 530, 700, 870] 
        for i, (text, command) in enumerate(buttons):
            self.create_rounded_button(x_positions[i], 180, 150, 50, text, command)

    def create_rounded_frame(self, x, y, width, height, text, value):
        canvas = Canvas(self.frame, width=width, height=height, bg="#B5B9F1", highlightthickness=0)
        canvas.place(x=x, y=y)
        radius = 20
        canvas.create_rectangle(
            radius, 0, width - radius, height, fill="white", outline="",
        )  
        canvas.create_rectangle(
            0, radius, width, height - radius, fill="white", outline=""
        )  
        canvas.create_oval(
            0, 0, radius * 2, radius * 2, fill="white", outline=""
        )  
        canvas.create_oval(
            width - radius * 2, 0, width, radius * 2, fill="white", outline=""
        )  
        canvas.create_oval(
            0, height - radius * 2, radius * 2, height, fill="white", outline=""
        )
        canvas.create_oval(
            width - radius * 2, height - radius * 2, width, height, fill="white", outline=""
        )  
        canvas.create_text(
            width / 2, height / 3, text=value, font=("Arial", 20, "bold"), fill="#333"
        )
        canvas.create_text(
            width / 2, height * 2 / 3, text=text, font=("Arial", 12), fill="#666"
        )

    def create_rounded_button(self, x, y, width, height, text, command):
        canvas = Canvas(self.frame, width=width, height=height, bg="#B5B9F1", highlightthickness=0)
        canvas.place(x=x, y=y)
        radius = 20

        normal_color = "white"
        hover_color = "#e6e6e6"  
        press_color = "#cccccc" 

        rect = canvas.create_rectangle(
            radius, 0, width - radius, height, fill=normal_color, outline=""
        )
        canvas.create_rectangle(
            0, radius, width, height - radius, fill=normal_color, outline=""
        )
        canvas.create_oval(
            0, 0, radius * 2, radius * 2, fill=normal_color, outline=""
        )
        canvas.create_oval(
            width - radius * 2, 0, width, radius * 2, fill=normal_color, outline=""
        )
        canvas.create_oval(
            0, height - radius * 2, radius * 2, height, fill=normal_color, outline=""
        )
        canvas.create_oval(
            width - radius * 2, height - radius * 2, width, height, fill=normal_color, outline=""
        )
        button_text = canvas.create_text(
            width / 2, height / 2, text=text, font=("Arial", 12, "bold"), fill="#333"
        )

        def on_enter(event):
            canvas.itemconfig(rect, fill=hover_color)

        def on_leave(event):
            canvas.itemconfig(rect, fill=normal_color)

        def on_press(event):
            canvas.itemconfig(rect, fill=press_color)

        def on_release(event):
            canvas.itemconfig(rect, fill=hover_color)
            command()  
        canvas.tag_bind(rect, "<Enter>", on_enter)
        canvas.tag_bind(button_text, "<Enter>", on_enter)

        canvas.tag_bind(rect, "<Leave>", on_leave)
        canvas.tag_bind(button_text, "<Leave>", on_leave)

        canvas.tag_bind(rect, "<Button-1>", on_press)
        canvas.tag_bind(button_text, "<Button-1>", on_press)

        canvas.tag_bind(rect, "<ButtonRelease-1>", on_release)
        canvas.tag_bind(button_text, "<ButtonRelease-1>", on_release)

    def logout(self):
        print("Logged out")

    
    def view_patient(self):
    # Clear any existing patient frames
        for widget in self.frame.winfo_children():
            if isinstance(widget, Frame) and widget.winfo_name() == "patient_frame":
                widget.destroy()
                    # Create a frame for the text box
        text_box_frame = Frame(self.frame, bg="#f8f9fa")

        text_box_frame.place(x=208, y=250, width=800, height=40)  # Adjust position and size as needed


        # Create a text box (Entry widget) to display patient info, centered and with no background
        patient_info_entry = Entry(
        text_box_frame,
        font=("Times new roman", 30),
        width=50,
        borderwidth=0,  # Remove border
        justify="center",  # Center the text
        fg="white",  # Text color
        bg="#808080"  # Background color
                )

        patient_info_entry.pack(expand=True)  # Center the text box in the frame

        # Example of displaying patient info
        example_patient_info = "Patient Data"
        patient_info_entry.insert(0, example_patient_info)


        # Create a modern frame for the patient data
        patient_frame = Frame(self.frame, name="patient_frame", bg="#f8f9fa", bd=0)

        patient_frame.place(x=208, y=300, width=800, height=400)  # Adjust position and size as needed


        # Create a canvas to hold the frame
        canvas = Canvas(patient_frame, bg="#f8f9fa", bd=0, highlightthickness=0)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(patient_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas to hold patient bars
        inner_frame = Frame(canvas, bg="#f8f9fa")
        canvas.create_window((0, 0), window=inner_frame, anchor='nw')
        header_framedoctor = Frame(inner_frame, bg="white", bd=2, relief="ridge")
        header_framedoctor.pack(fill=X, padx=10, pady=5)
        ###
        Label(header_framedoctor, text="id", bg="grey", fg="white", font=("Arial", 10, "bold"), width=15).pack(side=LEFT, padx=5, pady=5)
        Label(header_framedoctor, text="Name", bg="grey", fg="white", font=("Arial", 10, "bold"), width=15).pack(side=LEFT, padx=5, pady=5)
        Label(header_framedoctor, text="Username", bg="grey", fg="white", font=("Arial", 10, "bold"), width=15).pack(side=LEFT, padx=5, pady=5)
        Label(header_framedoctor, text="Age", bg="grey", fg="white", font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5, pady=5)
        Label(header_framedoctor, text="Phone", bg="grey", fg="white", font=("Arial", 10, "bold"), width=15).pack(side=LEFT, padx=5, pady=5)

        # Add some sample patient data


        connviewpateints = sqlite3.connect(db_path)
        ptviewpatient=connviewpateints.execute("""
                        SELECT id,name,username,age,gender,phone
                        FROM patient;                       
                        """)
        viewpateints=ptviewpatient.fetchall()
    
        sample_patients = []
        for patientdata in viewpateints:
            sample_patients.append({
                "id": patientdata[0], 
                "name": patientdata[1], 
                "username": patientdata[2],
                # "password":"HASED-PBKDF2",
                "age": patientdata[3],
                "gender": patientdata[4],
                "phone": patientdata[5],
            })
        print(sample_patients)
        # Create modern bars for each patient
        # for patient in sample_patients:
        #     patient_bar = Frame(inner_frame, bg="white", bd=2, relief="ridge", padx=10, pady=10)
        #     patient_bar.pack(fill=X, padx=10, pady=10)
        for index, patient in enumerate(sample_patients):
            # Alternate background colors for rows
            bg_color = "white" if index % 2 == 0 else "#f0f0f0"

            patient_bar = Frame(inner_frame, bg=bg_color, bd=2, relief="ridge", padx=10, pady=5)
            patient_bar.pack(fill=X, padx=10, pady=2)

            # Display patient information with styled labels
            Label(patient_bar, text=f"{patient['id']}", bg=bg_color, font=("Arial", 10),width=15).pack(side=LEFT, padx=5)
            Label(patient_bar, text=f"{patient['name']}", bg=bg_color, font=("Arial", 10),width=15).pack(side=LEFT, padx=5)
            Label(patient_bar, text=f"{patient['username']}", bg=bg_color, font=("Arial", 10),width=15).pack(side=LEFT, padx=5)
            # Label(patient_bar, text=f"{patient['password']}", bg=bg_color, font=("Arial", 10),width=15).pack(side=LEFT, padx=5)
            Label(patient_bar, text=f"{patient['age']}", bg=bg_color, font=("Arial", 10),width=15).pack(side=LEFT, padx=5)
            Label(patient_bar, text=f"{patient['phone']}", bg=bg_color, font=("Arial", 10),width=15).pack(side=LEFT, padx=5)
            # Label(doctor_bar, text=f"{doctorelement['phone']}", bg=bg_color, font=("Arial", 10), width=15).pack(side=LEFT, padx=5)
        # Update the scroll region of the canvas
        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def view_doc(self):
    # Clear any existing doctor frames
        for widget in self.frame.winfo_children():
            if isinstance(widget, Frame) and widget.winfo_name() == "doctor_frame":
                widget.destroy()
            text_box_frame2 = Frame(self.frame, bg="#f8f9fa")

            text_box_frame2.place(x=208, y=250, width=800, height=40)  


            doctor_info_entry = Entry(
                text_box_frame2,
                font=("Times new roman", 30),
                width=50,
                borderwidth=0,  
                justify="center",  
                fg="white",  
                bg="#808080"  
            )

            doctor_info_entry.pack(expand=True)  

            example_doctor_info = "Doctor Data"
            doctor_info_entry.insert(0, example_doctor_info)


        # Create a modern frame for the doctor data
        doctor_frame = Frame(self.frame, name="doctor_frame", bg="#f8f9fa", bd=0)

        doctor_frame.place(x=208, y=300, width=800, height=400)

        # Create a canvas to hold the frame
        canvas = Canvas(doctor_frame, bg="#f8f9fa", bd=0, highlightthickness=0)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(doctor_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas to hold doctor bars
        inner_frame = Frame(canvas, bg="#f8f9fa")
        canvas.create_window((0, 0), window=inner_frame, anchor='nw')

        # Add a fixed header
        header_frame = Frame(inner_frame, bg="white", bd=2, relief="ridge")
        header_frame.pack(fill=X, padx=10, pady=5)

        # Add header labels
        Label(header_frame, text="id", bg="grey", fg="white", font=("Arial", 10, "bold"), width=15).pack(side=LEFT, padx=5, pady=5)
        Label(header_frame, text="Name", bg="grey", fg="white", font=("Arial", 10, "bold"), width=15).pack(side=LEFT, padx=5, pady=5)
        Label(header_frame, text="Username", bg="grey", fg="white", font=("Arial", 10, "bold"), width=15).pack(side=LEFT, padx=5, pady=5)
        Label(header_frame, text="Age", bg="grey", fg="white", font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5, pady=5)
        Label(header_frame, text="Phone", bg="grey", fg="white", font=("Arial", 10, "bold"), width=15).pack(side=LEFT, padx=5, pady=5)
        Label(header_frame, text="Sessionfee", bg="grey", fg="white", font=("Arial", 10, "bold"), width=15).pack(side=LEFT, padx=5, pady=5)

        # Fetch doctor data

        connviewdoc = sqlite3.connect(db_path)

        ptviewdoc = connviewdoc.execute("""
                        SELECT id,name, username, age, gender, phone,SessionfeeEGP
                        FROM doctor;
                        """)
        viewdocs = ptviewdoc.fetchall()

        sample_doctors = []
        for doctordata in viewdocs:
            sample_doctors.append({
                "id": doctordata[0],
                "name": doctordata[1],
                "username": doctordata[2],
                "age": doctordata[3],
                "gender": doctordata[4],
                "phone": doctordata[5],
                "SessionfeeEGP": doctordata[6],
            })

        # Create modern bars for each doctor
        for index, doctorelement in enumerate(sample_doctors):
            # Alternate background colors for rows
            bg_color = "white" if index % 2 == 0 else "#f0f0f0"

            doctor_bar = Frame(inner_frame, bg=bg_color, bd=2, relief="ridge", padx=10, pady=5)
            doctor_bar.pack(fill=X, padx=10, pady=2)

            # Display doctor information with styled labels
            Label(doctor_bar, text=f"{doctorelement['id']}", bg=bg_color, font=("Arial", 10), width=15).pack(side=LEFT, padx=5)
            Label(doctor_bar, text=f"{doctorelement['name']}", bg=bg_color, font=("Arial", 10), width=15).pack(side=LEFT, padx=5)
            Label(doctor_bar, text=f"{doctorelement['username']}", bg=bg_color, font=("Arial", 10), width=15).pack(side=LEFT, padx=5)
            Label(doctor_bar, text=f"{doctorelement['age']}", bg=bg_color, font=("Arial", 10), width=10).pack(side=LEFT, padx=5)
            Label(doctor_bar, text=f"{doctorelement['phone']}", bg=bg_color, font=("Arial", 10), width=15).pack(side=LEFT, padx=5)
            Label(doctor_bar, text=f"{doctorelement['SessionfeeEGP']} EGP", bg=bg_color, font=("Arial", 10), width=15).pack(side=LEFT, padx=5)

        # Update the scroll region of the canvas
        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def add_doc(self):
        # Create a frame for the text box
        self.text_box_frame = Frame(self.frame, bg="#f8f9fa")
        self.text_box_frame.place(x=208, y=250, width=800, height=40)

        # Create a text box (Entry widget) to display patient info
        self.example_addDoctor_info_entry = Entry(
            self.text_box_frame,
            font=("Times new roman", 30),
            width=50,
            borderwidth=0,
            justify="center",
            fg="white",
            bg="#808080"
        )
        self.example_addDoctor_info_entry.pack(expand=True)
        self.example_addDoctor_info_entry.insert(0, "Add Doctor")

        # Create a modern frame for the doctor data
        self.adddoc_frame = Frame(self.frame, name="adddoc_frame", bg="#f8f9fa", bd=0)
        self.adddoc_frame.place(x=208, y=300, width=800, height=400)

        # Create a canvas to hold the frame
        self.canvas = Canvas(self.adddoc_frame, bg="#f8f9fa", bd=0, highlightthickness=0)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a scrollbar
        self.scrollbar = ttk.Scrollbar(self.adddoc_frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.config(scrollregion=self.canvas.bbox("all")))

        # Create a frame inside the canvas to hold doctor input fields
        self.inner_frame = Frame(self.canvas, bg="#f8f9fa")
        self.inner_frame.place(x=208, y=300, width=800, height=400)
        self.canvas.create_window((250, 0), window=self.inner_frame, anchor='nw')

        # Create labels and entry fields for the doctor form
        fields = [
            ("Name", "name"),
            ("Username", "username"),
            ("Password", "password"),
            ("Age", "age"),
            ("Phone", "phone"),
            ("Specialization", "specialization"),
            ("Qualification", "qualification"),
            ("Years of Experience", "years_of_experience"),
            ("SessionfeeEGP", "SessionfeeEGP"),
            ("Availability One", "availabilityone"),
            ("Availability Two", "availabilitytwo"),
            ("Rating", "rating"),
        ]

        self.entries = {}
        for label_text, field_name in fields:
            label = Label(self.inner_frame, text=label_text, bg="#f8f9fa")
            label.pack(pady=5)
            entry = Entry(self.inner_frame, width=50)
            entry.pack(pady=5)
            self.entries[field_name] = entry

        # Create gender selection
        self.gender_var = StringVar(value="Male")
        gender_label = Label(self.inner_frame, text="Gender", bg="#f8f9fa")
        gender_label.pack(pady=5)
        male_radio = Radiobutton(self.inner_frame, text="Male", variable=self.gender_var, value="Male", bg="#f8f9fa")
        female_radio = Radiobutton(self.inner_frame, text="Female", variable=self.gender_var, value="Female", bg="#f8f9fa")
        male_radio.pack(pady=5)
        female_radio.pack(pady=5)

        def add_doctor():
            """Add a new doctor to the database."""
            # Gather data from the entry fields
            doctor_data = {
                "name": self.entries["name"].get(),
                "username": self.entries["username"].get(),
                "password": self.entries["password"].get(),
                "age": self.entries["age"].get(),
                "phone": self.entries["phone"].get(),
                "specialization": self.entries["specialization"].get(),
                "qualification": self.entries["qualification"].get(),
                "years_of_experience": self.entries["years_of_experience"].get(),
                "SessionfeeEGP": self.entries["SessionfeeEGP"].get(),
                "availabilityone": self.entries["availabilityone"].get(),
                "availabilitytwo": self.entries["availabilitytwo"].get(),
                "rating": self.entries["rating"].get(),
                "gender": self.gender_var.get()
            }
            

            # Insert data into the database
            self.cursor.execute('''
                INSERT INTO doctor (name, username, password, age, gender, phone, specialization, qualification, 
                                     years_of_experience, SessionfeeEGP, availabilityone, availabilitytwo, 
                                     rating) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                doctor_data["name"],
                doctor_data["username"],
                doctor_data["password"],
                doctor_data["age"],
                doctor_data["gender"],
                doctor_data["phone"],
                doctor_data["specialization"],
                doctor_data["qualification"],
                doctor_data["years_of_experience"],
                doctor_data["SessionfeeEGP"],
                doctor_data["availabilityone"],
                doctor_data["availabilitytwo"],
                doctor_data["rating"]
            ))

            # Commit the changes and clear the entry fields
            self.conn.commit()
            clear_entries()

            # Optionally, you can show a success message
            print("Doctor added successfully!")

         # bt3ml clear ll labels yaaaa ((((((Ashraf)))))) ast5dmhaaa fe al dashboad bta3t al doctor w al patient
        def clear_entries():
            """Clear all entry fields after adding a doctor."""
            for entry in self.entries.values():
                entry.delete(0, tk.END)
            self.gender_var.set("Male")  # Reset gender selection to Male

        # Create a button to add the doctor
        add_button = Button(self.inner_frame, text="Add Doctor", command=add_doctor)
        add_button.pack(pady=20)

    def update_doc(self):
        print("Update Doc clicked")

        def update_doctor_fee():
            username = self.username_entry.get().strip()
            SessionfeeEGP = self.SessionfeeEGP_entry.get().strip()

            # Validate inputs
            if not username or not SessionfeeEGP:
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            try:
                SessionfeeEGP = float(SessionfeeEGP)
            except ValueError:
                messagebox.showerror("Error", "Session Fee must be a valid number.")
                return

            # Database operation
            try:
                conn = sqlite3.connect(db_path)  # Update with your database path if needed
                cursor = conn.cursor()

                # Check if the doctor exists
                cursor.execute("SELECT * FROM doctor WHERE username = ?", (username,))
                doctor = cursor.fetchone()

                if not doctor:
                    messagebox.showerror("Error", "Doctor not found.")
                    return

                # Update the session fee
                cursor.execute("UPDATE doctor SET SessionfeeEGP = ? WHERE username = ?", (SessionfeeEGP, username))
                conn.commit()
                messagebox.showinfo("Success", "Session Fee updated successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", str(e))
            finally:
                conn.close()

        # Destroy existing frame if present
        for widget in self.frame.winfo_children():
            if isinstance(widget, Frame) and widget.winfo_name() == "updatedoc_frame":
                widget.destroy()

        # Create a text box frame
        text_box_frame = Frame(self.frame, bg="#f8f9fa")
        text_box_frame.place(x=208, y=250, width=800, height=40)

        example_UpdateDoctor_info_entry = Entry(
            text_box_frame,
            font=("Times new roman", 30),
            width=50,
            borderwidth=0,
            justify="center",
            fg="white",
            bg="#808080"
        )
        example_UpdateDoctor_info_entry.pack(expand=True)
        example_UpdateDoctor_info_entry.insert(0, "Update Doctor")

        # Create a modern frame for the doctor data
        updatedoc_frame = Frame(self.frame, name="updatedoc_frame", bg="#f8f9fa", bd=0)
        updatedoc_frame.place(x=208, y=300, width=800, height=400)

        # Create a canvas to hold the frame
        canvas = Canvas(updatedoc_frame, bg="#f8f9fa", bd=0, highlightthickness=0)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(updatedoc_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas to hold doctor input fields
        inner_frame = Frame(canvas, bg="#f8f9fa")
        canvas.create_window((0, 0), window=inner_frame, anchor='nw')

        # Labels and Entry fields for Username and New Session Fee
        Label(inner_frame, text="Username:", font=("Times New Roman", 18), bg="#f8f9fa").grid(row=0, column=0, padx=20, pady=10, sticky=W)
        self.username_entry = Entry(inner_frame, font=("Times New Roman", 16), width=30)
        self.username_entry.grid(row=0, column=1, padx=20, pady=10)

        Label(inner_frame, text="New Session Fee (EGP):", font=("Times New Roman", 18), bg="#f8f9fa").grid(row=1, column=0, padx=20, pady=10, sticky=W)
        self.SessionfeeEGP_entry = Entry(inner_frame, font=("Times New Roman", 16), width=30)
        self.SessionfeeEGP_entry.grid(row=1, column=1, padx=20, pady=10)

        # Confirm button
        confirm_button = Button(inner_frame, text="Confirm", font=("Times New Roman", 16), bg="#808080", fg="white",
                                command=update_doctor_fee)
        confirm_button.grid(row=7, columnspan=2,padx=40, pady=20)


    def remove_doc(self):
        print("Remove Doc clicked")

        def delete_doctor():
            username = self.username_entry.get().strip()

            # Validate input
            if not username:
                messagebox.showerror("Error", "Please enter the username.")
                return

            # Database operation
            try:
                conn = sqlite3.connect(db_path)  # Update with your database path if needed
                cursor = conn.cursor()

                # Check if the doctor exists
                cursor.execute("SELECT * FROM doctor WHERE username = ?", (username,))
                doctor = cursor.fetchone()

                if not doctor:
                    messagebox.showerror("Error", "Doctor not found.")
                    return

                # Delete the doctor
                cursor.execute("DELETE FROM doctor WHERE username = ?", (username,))
                conn.commit()
                messagebox.showinfo("Success", "Doctor deleted successfully.")
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", str(e))
            finally:
                conn.close()

        # Destroy existing frame if present
        for widget in self.frame.winfo_children():
            if isinstance(widget, Frame) and widget.winfo_name() == "updatedoc_frame":
                widget.destroy()

        # Create a text box frame
        text_box_frame = Frame(self.frame, bg="#f8f9fa")
        text_box_frame.place(x=208, y=250, width=800, height=40)

        example_UpdateDoctor_info_entry = Entry(
            text_box_frame,
            font=("Times new roman", 30),
            width=50,
            borderwidth=0,
            justify="center",
            fg="white",
            bg="#808080"
        )
        example_UpdateDoctor_info_entry.pack(expand=True)
        example_UpdateDoctor_info_entry.insert(0, "Delete Doctor")

        # Create a modern frame for the doctor data
        updatedoc_frame = Frame(self.frame, name="updatedoc_frame", bg="#f8f9fa", bd=0)
        updatedoc_frame.place(x=208, y=300, width=800, height=400)

        # Create a canvas to hold the frame
        canvas = Canvas(updatedoc_frame, bg="#f8f9fa", bd=0, highlightthickness=0)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(updatedoc_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas to hold doctor input fields
        inner_frame = Frame(canvas, bg="#f8f9fa")
        canvas.create_window((0, 0), window=inner_frame, anchor='nw')

        # Label and Entry field for Username
        Label(inner_frame, text="Username:", font=("Times New Roman", 18), bg="#f8f9fa").grid(row=0, column=0, padx=20, pady=10, sticky=W)
        self.username_entry = Entry(inner_frame, font=("Times New Roman", 16), width=30)
        self.username_entry.grid(row=0, column=1, padx=20, pady=10)

        # Confirm button
        confirm_button = Button(inner_frame, text="Confirm", font=("Times New Roman", 16), bg="#808080", fg="white",
                                command=delete_doctor)
        confirm_button.grid(row=2, columnspan=2, padx=60, pady=20)


    def show_splash_then_exit(self):
        def splash_screen():
            # Create a new top-level window (splash screen)
            splash = ctk.CTkToplevel(self.master.root)
            splash.geometry("300x150+500+300")
            splash.title("Goodbye!")
            
            # Add a label to the splash screen
            ctk.CTkLabel(splash, text="Thank you for using DocHub!", font=("Arial", 14)).pack(pady=20)
            
            # Close splash after 2 seconds
            splash.after(2000, lambda: splash.destroy())
            
            # Close the main application after 2.5 seconds
            self.master.root.after(2500, self.master.root.destroy)

        # Run the splash screen in a separate thread to avoid blocking the main application
        Thread(target=splash_screen).start()


# if __name__ == "__main__":
#     frame = Tk()
#     app = AdminDashboard(frame)
#     frame.mainloop()

