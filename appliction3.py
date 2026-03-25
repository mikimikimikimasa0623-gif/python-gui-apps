import tkinter as tk
import random
import csv

def load_questions():
    QUESTIONS = []
    with open("英単語1.csv",mode="r",encoding="shift-JIS")as f:
            reader= csv.DictReader(f)
            for row in reader:
                QUESTIONS.append(row["word"])
    return QUESTIONS
   
QUESTIONS = load_questions()

def check_answer(event):
    user_input = entry.get()
    question = label_question.cget("text")

    if user_input==question:
        label_result.config(text="正解！",fg ="green")
        next_question()

    else:
        label_result.config(text ="不正解",fg="red")
    
    entry.delete(0,tk.END)

def next_question():
    new_q=random.choice(QUESTIONS)
    label_question.config(text=new_q)


root = tk.Tk()
root.title ("タイピング練習")
root.geometry("400x250")

label_info = tk.Label(root,text="下の文字を打ってEnterを押してね！",font=("MS Gothic",12))
label_info.pack(pady=10)

label_question= tk.Label(root,text="",font=("Arial",24,"bold"))
label_question.pack(pady=10)

entry = tk.Entry(root,font=("Arial",18))
entry.pack(pady=10)
entry.bind("<Return>",check_answer)

label_result = tk.Label(root,text="",font=("MS Gothic",14))
label_result.pack(pady=10)

next_question()

entry.focus_set()

root.mainloop()
