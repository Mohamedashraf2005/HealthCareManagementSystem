import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('1200x750')
root.title('Log In')
root.resizable(False, False)
root.config(background='#B5B9F1')

#switching Between pages here 
def switch_to_signin():
    root.destroy()  # Close the current window
    import SignIN  
    SignIN.main() 


f1 = Frame(width=1200, height=70, bg='#B5B9F1')  
f1.place(x=1, y=0)

btn1 = ctk.CTkButton(f1, text='Home', fg_color='#B5B9F1', text_color='black', border_width=2, border_color="black", corner_radius=20, hover_color='#A3A6F1')
btn1.place(x=15, y=20)

btn2 = ctk.CTkButton(f1, text='Doctors', fg_color='#B5B9F1', text_color='black', border_width=2, border_color="black", corner_radius=20, hover_color='#A3A6F1')
btn2.place(x=165, y=20)

btn3 = ctk.CTkButton(f1, text='About us', fg_color='#B5B9F1', text_color='black', border_width=2, border_color="black", corner_radius=20, hover_color='#A3A6F1')
btn3.place(x=315, y=20)

btn4 = ctk.CTkButton(f1, text='Contact us', fg_color='#B5B9F1', text_color='black', border_width=2, border_color="black", corner_radius=20, hover_color='#A3A6F1')
btn4.place(x=465, y=20)


f4 = Frame(width=500, height=400, bg='black') 
f4.place(x=700, y=180)


f_sign_in = Frame(width=600, height=500, bg='#B5B9F1')  
f_sign_in.place(x=0, y=200)


lab_sign_in_title = ctk.CTkLabel(f_sign_in, text="Sign Up", fg_color='#B5B9F1', text_color='black', font=('Helvetica', 28))
lab_sign_in_title.place(x=250, y=0)

lab_username = Label(f_sign_in, text="Name:", bg='#B5B9F1', font=("Arial", 16))  
lab_username.place(x=50, y=50)

entry_username = ctk.CTkEntry(f_sign_in, width=300, height=35, corner_radius=10, border_width=2, border_color="black", fg_color="white", text_color="black", placeholder_text="Enter your username")  
entry_username.place(x=160, y=50)

lab_name = Label(f_sign_in, text="Username:", bg='#B5B9F1', font=("Arial", 16))  
lab_name.place(x=50, y=100)

entry_name = ctk.CTkEntry(f_sign_in, width=300, height=35, corner_radius=10, border_width=2, border_color="black", fg_color="white", text_color="black", placeholder_text="Enter your name")  
entry_name.place(x=160, y=100)

lab_age = Label(f_sign_in, text="Age:", bg='#B5B9F1', font=("Arial", 16))  
lab_age.place(x=50, y=150)

entry_age = ctk.CTkEntry(f_sign_in, width=300, height=35, corner_radius=10, border_width=2, border_color="black", fg_color="white", text_color="black", placeholder_text="Enter your age")  
entry_age.place(x=160, y=150)

lab_phone = Label(f_sign_in, text="Phone:", bg='#B5B9F1', font=("Arial", 16))  
lab_phone.place(x=50, y=200)

entry_phone = ctk.CTkEntry(f_sign_in, width=300, height=35, corner_radius=10, border_width=2, border_color="black", fg_color="white", text_color="black", placeholder_text="Enter your phone")  
entry_phone.place(x=160, y=200)

lab_password = Label(f_sign_in, text="Password:", bg='#B5B9F1', font=("Arial", 16))  
lab_password.place(x=50, y=250)

entry_password = ctk.CTkEntry(f_sign_in, width=300, height=35, corner_radius=10, border_width=2, border_color="black", fg_color="white", text_color="black", placeholder_text="Enter your password", show="*")  
entry_password.place(x=160, y=250)

lab_gender = Label(f_sign_in, text="Gender", bg='#B5B9F1', font=("Arial", 16))  
lab_gender.place(x=50, y=300)

gender_var = StringVar(value="Male")  
radio_male = ctk.CTkRadioButton(f_sign_in, text="Male", variable=gender_var, value="Male")
radio_male.place(x=160, y=300)

radio_female = ctk.CTkRadioButton(f_sign_in, text="Female", variable=gender_var, value="Female")
radio_female.place(x=230, y=300)



btn_submit = ctk.CTkButton(f_sign_in, text="SIGN UP", fg_color='#A3A6F1', text_color='black', corner_radius=20,command=switch_to_signin)
btn_submit.place(x=250, y=350)


img = Image.open("Doctor.png").resize((500, 400))  # تأكد من اسم الملف بدون مسافات إضافية
img = ImageTk.PhotoImage(img)


img_label = Label(f4, image=img, bg='#B5B9F1')  
img_label.place(x=0, y=0)

root.mainloop()
