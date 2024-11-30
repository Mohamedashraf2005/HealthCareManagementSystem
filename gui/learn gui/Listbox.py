import tkinter as tk

# إنشاء نافذة
window = tk.Tk()
window.title("Listbox مثال")
window.geometry("300x300")
# إضافة قائمة
listbox = tk.Listbox(window)
listbox.pack()

# إضافة عناصر للقائمة
items = ["option 1", "option 2", "option 3"]
for item in items:
    listbox.insert(tk.END, item)

# زر لعرض العنصر المختار
def show_selected():
    selected_item = listbox.get(listbox.curselection())
    print(f"slected id: {selected_item}")

button = tk.Button(window, text="عرض العنصر", command=show_selected)
button.pack()

# تشغيل التطبيق
window.mainloop()

#? إيه اللي بيحصل؟
#! Listbox: قائمة عناصر.
#! insert(): تضيف عناصر للقائمة.
#! curselection(): تجيب العنصر المختار.