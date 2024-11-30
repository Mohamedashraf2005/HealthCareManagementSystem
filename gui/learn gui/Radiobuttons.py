import tkinter as tk

# إنشاء نافذة
window = tk.Tk()
window.title("Radiobuttons مثال")
window.geometry("300x300")
# متغير تخزين القيمة
selected_option = tk.StringVar(value="")

# إضافة أزرار اختيار
radio1 = tk.Radiobutton(window, text="choose 1", value="Option 1", variable=selected_option)
radio1.pack()

radio2 = tk.Radiobutton(window, text="choose 2", value="Option 2", variable=selected_option)
radio2.pack()

# زر لتأكيد الاختيار
def show_selection():
    print(f"the select: {selected_option.get()}")

button = tk.Button(window, text="show selection", command=show_selection)
button.pack()

# تشغيل التطبيق
window.mainloop()

#? إيه اللي بيحصل؟
#! StringVar: متغير بيخزن النص المرتبط بالخيار.
#! value: القيمة المرتبطة بكل زر.