from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3

class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x750+150+25")
        self.root.configure(bg="#B5B9F1")  
        self.root.title("Admin Dashboard")
        self.root.resizable(False, False)

        # self.logo_image()
        self.add_logout_button()
        self.add_welcome_message()
        self.add_statistics_with_curves()
        self.add_buttons_with_curves()

    # def logo_image(self):
    #     image = Image.open("logo.png").resize((150, 100))
    #     image = ImageTk.PhotoImage(image)
    #     label = Label(self.root, text="DocHub", compound="top", image=image, borderwidth=0,
    #                   font=("IM FELL Double Pica", 15, "bold"), bg="#B5B9F1")
    #     label.image = image  # Prevent image deletion from memory
    #     label.place(x=0, y=0)

    def add_logout_button(self):
        f1 = Frame(self.root, width=1100, height=50, bg='#B5B9F1')
        f1.place(x=150, y=25)
        
        button1 = ctk.CTkButton(f1,text='Log Out', fg_color='#336EA6', text_color='white', border_width=2, border_color='#336EA6', corner_radius=20, hover_color='#B5B9F1')
        button1.place(x=850, y=12)


    def add_welcome_message(self):
        welcome_label = Label(self.root, text="Welcome, Admin..", font=("Arial", 18, "bold"), bg="#B5B9F1", fg="#fff")
        welcome_label.place(x=530, y=30)

    def add_statistics_with_curves(self):
        conn = sqlite3.connect(r"D:\FAI\03SWE\Project\HCMS_Github\database\HCMSclinic.db")
        ptpatient=conn.execute("""
                        SELECT MAX(id)
                        FROM patient;                       
                        """)
        ptdoctor=conn.execute("""
                        SELECT MAX(id)
                        FROM doctor;
                        """)
        numberofpateints=ptpatient.fetchone()
        numberofdoctors=ptdoctor.fetchone()
        conn.commit()
        conn.close()
        stats = [
            ("Patients",numberofpateints),
            ("Doctors", numberofdoctors),
            ("Balance", "78,000$"),
        ]

        x_positions = [350, 550, 750]  
        for i, (text, value) in enumerate(stats):
            self.create_rounded_frame(x_positions[i], 80, 150, 100, text, value)#y-axis,w-frame,h-frame,text-frame

    def add_buttons_with_curves(self):
        buttons = [
            ("View Patients", self.view_patient),
            ("View Doc", self.view_doc),
            ("Add Doc", self.add_doc),
            ("Update Doc", self.update_doc),
            ("Remove Doc", self.remove_doc),
        ]

        x_positions = [230,390, 550, 710, 870] 
        for i, (text, command) in enumerate(buttons):
            self.create_rounded_button(x_positions[i], 185, 150, 50, text, command)

    def create_rounded_frame(self, x, y, width, height, text, value):
        canvas = Canvas(self.root, width=width, height=height, bg="#B5B9F1", highlightthickness=0)
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
        canvas = Canvas(self.root, width=width, height=height, bg="#B5B9F1", highlightthickness=0)
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
        for widget in self.root.winfo_children():
            if isinstance(widget, Frame) and widget.winfo_name() == "patient_frame":
                widget.destroy()
                    # Create a frame for the text box
        text_box_frame = Frame(self.root, bg="#f8f9fa")
        text_box_frame.place(x=250, y=250, width=800, height=40)  # Adjust position and size as needed

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
        patient_frame = Frame(self.root, name="patient_frame", bg="#f8f9fa", bd=0)
        patient_frame.place(x=250, y=300, width=800, height=400)  # Adjust position and size as needed

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
        connviewpateints = sqlite3.connect(r"D:\FAI\03SWE\Project\HCMS_Github\database\HCMSclinic.db")
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
        for widget in self.root.winfo_children():
            if isinstance(widget, Frame) and widget.winfo_name() == "doctor_frame":
                widget.destroy()
            text_box_frame2 = Frame(self.root, bg="#f8f9fa")
            text_box_frame2.place(x=250, y=250, width=800, height=40)  

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
        doctor_frame = Frame(self.root, name="doctor_frame", bg="#f8f9fa", bd=0)
        doctor_frame.place(x=250, y=300, width=800, height=400)

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
        connviewdoc = sqlite3.connect(r"D:\FAI\03SWE\Project\HCMS_Github\database\HCMSclinic.db")
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
        print("Add clicked")

    def update_doc(self):
        print("Update Doc clicked")

    def remove_doc(self):
        print("Remove Doc clicked")


if __name__ == "__main__":
    root = Tk()
    app = AdminDashboard(root)
    root.mainloop()