import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.geometry('1200x750+150+25')
root.title('Patient page')
root.resizable(False, False)
root.config(background='#B5B9F1')
root.iconbitmap(r'D:\FAI\03SWE\Project\HCMS_Github\gui\PHOTO\logoIcon.ico')

def logo_image():
    image = Image.open(r"D:\FAI\03SWE\Project\HCMS_Github\gui\PHOTO\logo.png").resize((110, 100)).convert("RGBA")
    datas = image.getdata()
    new_data = []
    for item in datas:
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    image.putdata(new_data)
    image = ImageTk.PhotoImage(image)
    label = Label(root, text='DOCHUB' ,compound="top", image=image, borderwidth=0,
                  font=("IM FELL Double Pica", 13, "bold"), bg="#B5B9F1",fg='#194C7C')
    label.image = image
    label.place(x=0, y=0)
    return label

logo_img = logo_image()
#frame of logout
f1=Frame(width=1100,height=50,bg='#B5B9F1')
f1.place(x=150,y=25)

button1=ctk.CTkButton(f1,text='Log Out',fg_color='#336EA6',text_color='white',border_width=2,border_color='#336EA6',corner_radius=20,hover_color='#B5B9F1')
button1.place(x=850,y=12)

#frame of welcome
f2=Frame(width=1200,height=60,bg='#B5B9F1')
f2.place(x=0,y=130)

lab1=ctk.CTkLabel(f2,text='Welcome,############',text_color='black',font=('Adobe Garamond Pro',30,'bold'))
lab1.place(x=400,y=0)


#main frame of appointment request
f3=ctk.CTkFrame(root,width=745,height=350,corner_radius=20,fg_color='white')
f3.place(x=50,y=230)

lab2=Label(f3,text='Appointment requests',fg='black',bg='white',font=("Felix Titling",18,'bold'))
lab2.place(x=10,y=10)

# Fetch data from the database
conn = sqlite3.connect(r"D:\FAI\03SWE\Project\HCMS_Github\database\HCMSclinic.db")
ptpatientdasboard = conn.execute("""
    SELECT name, specialization,SessionfeeEGP, availabilityone, availabilitytwo, rating
    FROM doctor;
""")
data = ptpatientdasboard.fetchall()
conn.close()

f5 = ctk.CTkScrollableFrame(f3, width=710, height=260, corner_radius=10)
f5.place(x=5, y=55)

# New columns to be used for the header
columns = ["Name", "Category", "Fee", "Time 1", "Time 2", "Rating"]

# Create the new column headers
for col_index, col_name in enumerate(columns):
    ctk.CTkLabel(f5, text=col_name, font=('Arial', 14, 'bold'), text_color='black').grid(row=0, column=col_index, padx=5, pady=2)

# Fetch data from the database
conn = sqlite3.connect(r"D:\FAI\03SWE\Project\HCMS_Github\database\HCMSclinic.db")
ptpatientdasboard = conn.execute("""
    SELECT name, specialization, SessionfeeEGP, availabilityone, availabilitytwo, rating
    FROM doctor;
""")
data = ptpatientdasboard.fetchall()
conn.close()

# Populate the data dynamically under the new columns
for row_index, row in enumerate(data, start=1):  # start=1 to leave the first row for headers
    for col_index, value in enumerate(row):
        ctk.CTkLabel(f5, text=str(value), font=('arial', 12), text_color='black').grid(row=row_index, column=col_index, padx=5, pady=2)

    # Create a unique StringVar for each row's radio buttons
    radio_vars=[]
    radio_var = ctk.StringVar(value='other')
    radio_vars.append(radio_var)  # Store it to prevent garbage collection
    
    # Add radio buttons for "Yes" and "No"
    ctk.CTkRadioButton(f5, text='Yes', value='yes', variable=radio_var, fg_color='green', hover_color='green').grid(row=row_index, column=len(columns), padx=2, pady=2)
    ctk.CTkRadioButton(f5, text='No', value='no', variable=radio_var, fg_color='red', hover_color='red').grid(row=row_index, column=len(columns) + 1, padx=2, pady=2) 


#frame of patient info  
f6=ctk.CTkFrame(root,width=300,height=210,corner_radius=20,fg_color='white')
f6.place(x=870,y=230)
#patient info
info_lab=ctk.CTkLabel(f6,text='Patient INFO ',text_color='black',font=('Felix Titling',20))
info_lab.place(x=70,y=20)
#patient name
name_lab=ctk.CTkLabel(f6,text='Name :',text_color='black',font=('Felix Titling',20))
name_lab.place(x=15,y=60)
#patient age
age_lab=ctk.CTkLabel(f6,text='Age :',text_color='black',font=('Felix Titling',20))
age_lab.place(x=15,y=100)
#patient gender
gender_lab=ctk.CTkLabel(f6,text='Gender :',text_color='black',font=('Felix Titling',20))
gender_lab.place(x=15,y=140)
#patient book label
book_lab=ctk.CTkLabel(f6,text='Booked :',text_color='black',font=('Felix Titling',20))
book_lab.place(x=15,y=180)
#image 
img=Image.open(r'D:\FAI\03SWE\Project\HCMS_Github\gui\PHOTO\fepatient.png').resize((300,300))
img = ImageTk.PhotoImage(img)
img_label = Label(root, image=img, bg='#B5B9F1')  
img_label.place(x=870,y=440)

#confirm buuton
confirm_button=ctk.CTkButton(root,text='Confirmation',text_color='white',fg_color='#7579B9',corner_radius=20,hover_color='#B5B9F1',font=('arial',20),border_width=2,border_color='#7579B9')
confirm_button.place(x=350,y=600)
root.mainloop()
