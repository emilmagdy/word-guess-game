import random
import tkinter as tk
from game_logic import word_list


# variables
green = "#4bf80f"
font = ("comic sense", 60)
letters =[]
word = "GRADE"
btn_index = 0
count = 0
guess =""
char_not_present=[]
winner = False

# game main loop

root = tk.Tk()
root.title("Wordle")
root.geometry("600x900")


# new game 
def new_game():
    global btn_index, winner, count , char_not_present
    layout()
    
    root.bind("<Key>"  , key_press)
    

menu_bar = tk.Menu(root)
my_menu = tk.Menu(menu_bar)
my_menu.add_command(label="New Game", command = new_game)
root.config(menu = my_menu)
label = tk.Label(root , text= "Wordle",  font = ("arial", 30))
label.pack(padx=10, pady= 10)
frame = tk.Frame(root)
frame.pack()
label2 = tk.Label(root , text ="Good Job...\n  You guessed it!", bg="yellow", font = ("arial", 50))

# word check
def word_check(guess):
    global btn_index , winner
    btn_index -= 5
    for i in range(5):
        if letters[btn_index + i].cget("text")== word[i]:
            letters[btn_index + i].config(bg=green)
            
        elif letters[btn_index + i].cget("text") in word:
            letters[btn_index + i].config(bg="yellow")
        else :
            letters[btn_index + i].config(bg="gray")
            char_not_present.append(letters[btn_index + i].cget("text"))
                                    
    if guess == word:
         winner = True
         label2.pack()
    
    btn_index += 5           

# key event
def key_press(event):
    global btn_index, count, guess , winner
    if winner == False:
        letter = event.char.upper()
        if letter not in char_not_present and letter.isalpha():
            letters[btn_index].config(text= letter)
            guess += letter
            btn_index += 1
            count += 1
            if count % 5 == 0:
                word_check(guess)
                guess =""

# layout 
def layout():
    for row in range(6):
        for col in range(5):
            btn = tk.Button(frame, text = "" ,width=1, font = font, bg = "white")
            btn.grid(row = row, column = col)
            letters.append(btn)


    

new_game()

root.mainloop()
