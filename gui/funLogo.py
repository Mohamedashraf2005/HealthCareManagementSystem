from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

root = Tk()
root.geometry("1280x832")

# Function to create a transparent logo
def logo_image():
    image = Image.open("logo.png").resize((150, 100)).convert("RGBA")
    datas = image.getdata()
    new_data = []
    for item in datas:
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    image.putdata(new_data)
    image = ImageTk.PhotoImage(image)
    label = Label(root, text="BANANA CLINIC", compound="top", image=image, borderwidth=0,
                  font=("IM FELL Double Pica", 15, "bold"), bg="#B5B9F1")
    label.image = image
    label.place(x=0, y=0)
    return label

logo_img = logo_image()

root.mainloop()