import tkinter as tk

# نافذة
window = tk.Tk()
window.title(" Grid")
window.geometry("300x300")
selected_option = tk.StringVar(value="")
# مكونات
label = tk.Label(window, text="name:" )
label.grid(row=0, column=0)

entry = tk.Entry(window, textvariable=selected_option)
entry.grid(row=0, column=1)


# زر لحفظ القيمة
def save_name():
    print(f" date is: {selected_option.get()}")
    

button = tk.Button(window, text="save", command=save_name)
button.grid(row=1, column=0, columnspan=2)

# تشغيل
window.mainloop()

#? إيه اللي بيحصل؟
#! row & column: تحدد مكان المكون في الشبكة.
#! columnspan: يخلي المكون يغطي أكثر من عمود.