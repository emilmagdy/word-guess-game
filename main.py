import random
import tkinter as tk
from generate_word_list import word_list


# variables

font = ("comic sense", 30)
letters =[]
word = random.choice(word_list).upper()
btn_index = 0
count = 0
guess =""
char_not_present=[]
winner = False

# game main loop

root = tk.Tk()
root.title("Wordle")
root.geometry("600x1000")
root.configure(bg= "black")
label = tk.Label(root , text= "WORDLE", bg= "black", foreground= "white", font = ("sanserif", 50))
label.pack(padx=10, pady= 10)
frame = tk.Frame(root)
frame.pack()
label2 = tk.Label(root , text ="Good Job...\n  You guessed it!", bg = "black",foreground= "yellow", font = ("arial", 20))
label3 = tk.Label(root,  font = ("arial", 20),bg = "black", foreground= "yellow", text="Not In word list")
# word check
def word_check(guess):
    global btn_index , winner 
    if guess.lower() not in word_list:
        label3.pack()
        btn_index -= 5
        return

    btn_index -= 5
    for i in range(5):
        if letters[btn_index + i].cget("text")== word[i]:
            letters[btn_index + i].config(bg="green")
            letters[btn_index + i].config(activebackground = "green")
            
        elif letters[btn_index + i].cget("text") in word:
            letters[btn_index + i].config(bg="orange")
            letters[btn_index + i].config(activebackground = "orange")
        
        else :
            letters[btn_index + i].config(bg="gray")
            letters[btn_index + i].config(activebackground = "gray")

            char_not_present.append(letters[btn_index + i].cget("text"))
                                    
    if guess == word:
         winner = True
         
         label2.pack()
    
    btn_index += 5           

# key event
def key_press(event):
    global btn_index, count, guess , winner
    if winner:
        return
    label3.forget()
    
    if event.keysym == "BackSpace":
        if btn_index> 0 and  (btn_index ) % 5 > 0:
            btn_index -= 1
            letters[btn_index].config(text ="")
            count -= 1
            guess = guess[: -1]
    
    letter = event.char.upper()
    letters[btn_index].focus()
    if letter not in char_not_present and letter.isalpha():
        letters[btn_index].config(text= letter)
        guess += letter
        btn_index += 1
        count += 1
        if count % 5 == 0:
            word_check(guess)
            guess =""

# Grid Layout for the letters entry 
def layout():
    for row in range(6):
        for col in range(5):
            btn = tk.Button(frame,foreground="white", bg= "black", activebackground= "black", text = "" ,width=1, height=1, font = font ,highlightthickness=2, highlightbackground="blue")
            btn.grid(row = row, column = col, padx=1, pady=1)
            letters.append(btn)

# New Game
def new_game():
    global winner, btn_index, letters, count, char_not_present, word, guess
    word = random.choice(word_list).upper()
    print(word)
    guess =""
    count = 0
    char_not_present =[]
    letters = []
    btn_index = 0
    winner = False
    label2.forget()
    
    root.bind("<Key>"  , key_press)
    layout()

new_game()


menu_bar = tk.Menu(root)
my_menu = tk.Menu(menu_bar)
my_menu.add_command(label="New Game", command = new_game)
root.config(menu = my_menu)

root.mainloop()
