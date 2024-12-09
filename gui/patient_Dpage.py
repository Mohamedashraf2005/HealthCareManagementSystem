import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry('1200x750+150+25')
root.title('Patient page')
root.resizable(False, False)
root.config(background='#B5B9F1')
root.iconbitmap('logo.ico')

def logo_image():
    image = Image.open("D:\paython tasks\SWE project\logo-removebg.png").resize((110, 100)).convert("RGBA")
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

lab1=ctk.CTkLabel(f2,text='Welcome,############',text_color='black',font=('Adobe Garamond Pro',35,'bold'))
lab1.place(x=270,y=15)


#main frame of appointment request
f3=ctk.CTkFrame(root,width=692,height=350,corner_radius=20,fg_color='white')
f3.place(x=100,y=230)

lab2=Label(f3,text='Appointment requests',fg='black',bg='white',font=("Felix Titling",20,'bold'))
lab2.place(x=20,y=10)

#frame of scroll frame
f5=ctk.CTkScrollableFrame(f3,width=658,height=220,label_text='Name \t\tCategory \t\t\tFee \t\tTime  \t\tDone',corner_radius=10)
f5.place(x=5,y=55)



#label of name ,age ...etc
ctk.CTkLabel(f5,text='label',font=('arial',15)).grid(column=1,row=1)
ctk.CTkLabel(f5,text='\t\t\t\t\t\t\t\t          ').grid(row=1,column=198)
#radio buttons in scroll frame
radio_var=ctk.StringVar(value='other')
ctk.CTkRadioButton(f5,text='Yes',value='yes',variable=radio_var,fg_color='green',hover_color='green',).grid(row=1,column=199)
ctk.CTkRadioButton(f5,text='No',value='no',variable=radio_var,fg_color='red',hover_color='red',).grid(row=1,column=200)



#frame of patient info  
f6=ctk.CTkFrame(root,width=300,height=210,corner_radius=20,fg_color='white')
f6.place(x=850,y=230)
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
img=Image.open('fepatient.png').resize((300,300))
img = ImageTk.PhotoImage(img)
img_label = Label(root, image=img, bg='#B5B9F1')  
img_label.place(x=800,y=440)

#confirm buuton
confirm_button=ctk.CTkButton(root,text='Confirmation',text_color='white',fg_color='#7579B9',corner_radius=20,hover_color='#B5B9F1',font=('arial',20),border_width=2,border_color='#7579B9')
confirm_button.place(x=400,y=600)




root.mainloop()
