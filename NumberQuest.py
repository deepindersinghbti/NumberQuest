import tkinter as tk
from random import randint

attempts = 3

def guess_num():
    global attempts
    user_input = int(entry.get())
    if user_input == num:
        result_label.config(text="Congratulations! You guessed it right.")
        entry.pack_forget()
        submit_button.pack_forget()
        attempts_label.pack_forget()
    elif attempts == 1:
        result_label.config(text="Game Over! Better luck next time.")
        entry.pack_forget()
        submit_button.pack_forget()
        attempts_label.pack_forget()
    else:
        if user_input < num:
            result_label.config(text="Too low!")
        elif user_input > num:
            result_label.config(text="Too high!")
        attempts -= 1
        attempts_label.config(text=f"Remaining attempts: {attempts}")

num = randint(0, 9)

root = tk.Tk()
root.title("NumberQuest")
root.minsize(280, 100)

frame = tk.Frame(root)
frame.pack(expand=True)

entry = tk.Entry(frame, width=30)
entry.pack()

submit_button = tk.Button(frame, text="Submit", command=guess_num)
submit_button.pack()

result_label = tk.Label(frame, text="Number set! Try guessing the number now.")
result_label.pack()

attempts_label = tk.Label(frame, text=f"Remaining attempts: {attempts}")
attempts_label.pack()

root.mainloop()