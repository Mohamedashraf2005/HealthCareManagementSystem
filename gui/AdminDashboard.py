from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk


class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x750+150+25")
        self.root.configure(bg="#B5B9F1")  
        self.root.title("Admin Dashboard")
        self.root.resizable(False, False)

        self.logo_image()
        self.add_logout_button()
        self.add_welcome_message()
        self.add_statistics_with_curves()
        self.add_buttons_with_curves()

    def logo_image(self):
        image = Image.open("logo.png").resize((150, 100))
        image = ImageTk.PhotoImage(image)
        label = Label(self.root, text="DocHub", compound="top", image=image, borderwidth=0,
                      font=("IM FELL Double Pica", 15, "bold"), bg="#B5B9F1")
        label.image = image  # Prevent image deletion from memory
        label.place(x=0, y=0)

    def add_logout_button(self):
        f1 = Frame(self.root, width=1100, height=50, bg='#B5B9F1')
        f1.place(x=150, y=25)
        
        button1 = ctk.CTkButton(f1,text='Log Out', fg_color='#336EA6', text_color='white', border_width=2, border_color='#336EA6', corner_radius=20, hover_color='#B5B9F1')
        button1.place(x=850, y=12)


    def add_welcome_message(self):
        welcome_label = Label(self.root, text="Welcome, Admin..", font=("Arial", 18, "bold"), bg="#B5B9F1", fg="#2D82FF")
        welcome_label.place(x=530, y=150)

    def add_statistics_with_curves(self):
        stats = [
            ("Patients Treated", "1053"),
            ("N Doc", "1053"),
            ("Balance", "1053"),
        ]

        x_positions = [350, 550, 750]  
        for i, (text, value) in enumerate(stats):
            self.create_rounded_frame(x_positions[i], 300, 150, 100, text, value)

    def add_buttons_with_curves(self):
        buttons = [
            ("View Doc", self.view_doc),
            ("Add", self.add_doc),
            ("Update Doc", self.update_doc),
            ("Remove Doc", self.remove_doc),
        ]

        x_positions = [250, 450, 650, 850] 
        for i, (text, command) in enumerate(buttons):
            self.create_rounded_button(x_positions[i], 600, 150, 50, text, command)

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

    def view_doc(self):
        print("View Doc clicked")

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
