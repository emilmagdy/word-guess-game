import tkinter as tk
from tkinter import messagebox
from game_logic import CharList, word_list, secret_word

print(secret_word)
char_not_present =[]


def on_key(event, index):
    value = guess[index].get()

    # Only keep first character and make it uppercase
    if len(value) > 1:
        guess[index].delete(1, tk.END)

    if  value.isdigit() or value in char_not_present:
        guess[index].delete(0, tk.END)
    else:
        guess[index].delete(0, tk.END)
        guess[index].insert(0, value.upper())

        # Move to next entry automatically
        if index < len(guess) - 1:
            guess[index + 1].focus()
    

def on_submit():
    word = "".join(e.get() for e in guess)
    if word.lower() not in word_list:
        messagebox.showerror("Invalid Word", "Please Enter a Valid Word")
    
    for i in range(len(guess)):
        if guess[i].get().lower() in secret_word:
            guess[i].config(bg= "yellow")
        else:
            guess[i].config(bg="gray")
            char_not_present.append(guess[i].get())
        if guess[i].get().lower() == secret_word[i]:
                guess[i].config(bg = "lightgreen")
    
    new_guess()




    
# setup the main window
root = tk.Tk()
root.title( "Word Guess Game")
root.geometry("800x800")

# Setup the labels
Titile_label = tk.Label(root, text="Word Guess Game", font =("Arial", 60), justify="center", foreground="darkblue")
Titile_label.pack(padx=20, pady=20)

instr_label = tk.Label(root, text=" Make a guess of 5 letters word", font =("Arial",30))
instr_label.pack(padx=20 ,pady=20)

# Setup the entry feilds
entry_frame = tk.Frame(root)
entry_frame.pack()
guess = []
for i in range(5):
         e=tk.Entry(entry_frame, width = 3 , font = ("Arial", 25), justify="center")
         e.bind("<KeyRelease>", lambda event, idx=i: on_key(event, idx))
         e.grid(row=0, column=i)
         guess.append(e)
  


submit_button = tk.Button(entry_frame, text="Submit", font=("Arial", 25),bg="lightblue", command = on_submit)
submit_button.grid(row = 0, column = 6) 





root.mainloop()
