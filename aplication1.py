import tkinter as tk
import random

# --- 準備：最初に1回だけ決める ---
answer = random.randint(1, 100)
count = 5

def reset_game():
    global answer, count
    answer = random.randint(1, 100)
    count = 5
  
    # 1 見た目を初期化（.configを使う！）
    label.config(text="1〜100の数字を当ててね")
    result_label.config(text="ここに結果が出ます", fg="black")
    entry.delete(0, tk.END) # 入力欄を空に
    button.config(state="normal") # 予想ボタンを復活させる

def judge():
    global count
    # 入力された数字を取る
    guess = int(entry.get())
    
    # 判定（whileは使わず、ifだけで1回判定する）
    if guess == answer:
        result_label.config(text="正解！おめでとう！", fg="red")
    elif guess < answer:
        result_label.config(text="もっと大きいよ！")
        entry.delete(0, tk.END) # 0文字目から最後まで（END）を消す
        count -=1
        label.config(text = f"解答回数はあと{count}回です")
    else:
        result_label.config(text="もっと小さいよ！")
        entry.delete(0, tk.END) # 0文字目から最後まで（END）を消す
        count -=1
        label.config(text = f"解答回数はあと{count}回です")
    
    if count ==0:
        result_label.config(text = f"解答終了です。答えは{answer}でした。")
        button.config(state = "disabled")
        
# --- 画面を作る ---
root = tk.Tk()
root.title("GUI版 数あてゲーム")
root.geometry("300x200")

label = tk.Label(root, text="1〜100の数字を当ててね")
label.grid(row = 0,column = 0,columnspan=3,padx=10,pady=20)

entry = tk.Entry(root)
entry.grid(row = 1,column = 0,padx = 10,pady =10)

button = tk.Button(root, text="予想する", command=judge)
button.grid(row=1,column =1,padx=10,pady =10)

reset_button = tk.Button(root,text="リセット",command = reset_game)
reset_button.grid(row =1,column = 2 ,padx =10,pady =10)

result_label = tk.Label(root, text="ここに結果が出ます")
result_label.grid(row =2,column =0,columnspan=3,padx=10,pady =20)

root.mainloop()