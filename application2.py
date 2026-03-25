import tkinter as tk

total_price = 0

def add_item():
    global total_price
    item = entry_item.get()
    price = entry_price.get()
    price_text = entry_price.get()

    try:
        price =int(price_text)
        if item and price:
            listbox.insert(tk.END,f"{item}:{price}円")
            total_price += int(price)
            total_label.config(text = f"合計金額：{total_price}円")

            entry_item.delete(0,tk.END)
            entry_price.delete(0,tk.END)
    
    except:
        total_label.config(text="エラー！金額は数字を入れて下さい",fg ="red")
        entry_price.delete(0,tk.END)

root = tk.Tk()
root.title("簡易お小遣い帳")
root.geometry("300x400")

tk.Label(root,text="品名:").pack()
entry_item= tk.Entry(root)
entry_item.pack()

tk.Label(root,text = "金額:").pack()
entry_price = tk.Entry(root)
entry_price.pack()

total_label = tk.Label(root,text ="合計金額：0円",font=("MS Gothic",12,"bold"))
total_label.pack(pady = 5)

button_add = tk.Button(root,text ="追加",command = add_item)
button_add.pack()

listbox = tk.Listbox(root)
listbox.pack(pady =10,fill="both",expand=True)

root.mainloop()