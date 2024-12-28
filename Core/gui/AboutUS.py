import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image

class About_Us:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x750+150+25')
        self.root.title('AboutUs page')
        self.root.resizable(False, False)
        self.root.config(background='#B5B9F1')

        self.logo_image()
        self.create_widgets()

        
        self.male_y = 250 
        self.female_y = 350

        self.Male_Section("Anas Elgezawy", "anaselgezawy@gmail.com")
        self.Male_Section("Ali Elbahrawy", "ali.fathy.ali20@gmail.com")
        self.Male_Section("Mohamed Ahmed", "aboalianamedo@gmail.com")
        self.Male_Section("Mohamed Ashraf", "mohamedachrvf@gmail.com")
        self.Female_Section("Eman Hekal", "hekaleman103@gmail.com")
        self.Female_Section("Mariam Ahmed", "anaselgezawy@gmail.com")

    def logo_image(self):
        image = Image.open(r"D:\\Project\\Python Folder\\logo.png").resize((150, 100)).convert("RGBA")
        datas = image.getdata()
        new_data = []
        for item in datas:
            if item[0] > 200 and item[1] > 200 and item[2] > 200:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
        image.putdata(new_data)
        image = ImageTk.PhotoImage(image)
        label = Label(self.root, text='DocHub', compound="top", image=image, borderwidth=0,
                      font=("IM FELL Double Pica", 13, "bold"), bg="#B5B9F1", fg='#194C7C')
        label.image = image
        label.place(x=0, y=0)

    def create_widgets(self):
        f2 = Frame(width=900, height=100, bg='#B5B9F1')  
        f2.place(x=1, y=120)

        lab1 = ctk.CTkLabel(f2, text='About US', fg_color='black', text_color='white', font=('Helvetica', 33), corner_radius=15)
        lab1.place(x=510, y=15)

    def Male_Section(self, name, Email):
        male_icon = Image.open(r"C:\Users\lOl\Documents\GitHub\DocHub\Core\gui\PHOTO\ManIco.png").resize((50, 50))
        male_icon = ImageTk.PhotoImage(male_icon)
        male_label = Label(self.root, image=male_icon, compound="left",
                           text=f"  {name} \n  {Email}",
                           font=("Helvetica", 15), bg="#B5B9F1", fg="black")
        male_label.image = male_icon
        male_label.place(x=150, y=self.male_y)  
        self.male_y += 100  

    def Female_Section(self, name, Email):
        female_icon = Image.open(r"C:\Users\lOl\Documents\GitHub\DocHub\Core\gui\PHOTO\FemaleIco.png").resize((50, 50))
        female_icon = ImageTk.PhotoImage(female_icon)
        female_label = Label(self.root, image=female_icon, compound="left",
                             text=f"  {name} \n  {Email}",
                             font=("Helvetica", 15), bg="#B5B9F1", fg="black")
        female_label.image = female_icon
        female_label.place(x=750, y=self.female_y)  
        self.female_y += 100  


if __name__ == "__main__":
    root = Tk()
    app = About_Us(root)
    root.mainloop()
