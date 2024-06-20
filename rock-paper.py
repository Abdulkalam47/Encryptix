from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Rock-Paper-Scissor")
root.configure(background="#9b59b6")

rock_img = ImageTk.PhotoImage(Image.open("C:\\Users\\ABDULKALAM SOLANKI\\Desktop\\Software Projects\\intership\\user-rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("C:\\Users\\ABDULKALAM SOLANKI\\Desktop\\Software Projects\\intership\\paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("C:\\Users\\ABDULKALAM SOLANKI\\Desktop\\Software Projects\\intership\\user-scissors.png"))
rock_comp_img = ImageTk.PhotoImage(Image.open("C:\\Users\\ABDULKALAM SOLANKI\\Desktop\\Software Projects\\intership\\comp-rock.png"))
paper_comp_img = ImageTk.PhotoImage(Image.open("C:\\Users\\ABDULKALAM SOLANKI\\Desktop\\Software Projects\\intership\\paper-comp.png"))
scissor_comp_img = ImageTk.PhotoImage(Image.open("C:\\Users\\ABDULKALAM SOLANKI\\Desktop\\Software Projects\\intership\\scissors.png"))

user_label = Label(root, image=rock_img, bg="#e66465")
comp_label = Label(root, image=rock_comp_img, bg="#e66465")

comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

rock = Button(root, width=20, height=2, text="ROCK", bg="#ff3e4d", fg="white", command=lambda: updateChoice("rock"))
rock.grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#fad02e", fg="white", command=lambda: updateChoice("paper"))
paper.grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0abde3", fg="white", command=lambda: updateChoice("scissor"))
scissor.grid(row=2, column=3)

user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

def updateMessage(x):
    msg['text'] = x
    
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

choices = ["rock", "paper", "scissor"]
def updateChoice(x):
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_comp_img)
    elif compChoice == "paper":
        comp_label.configure(image=paper_comp_img)
    else:
        comp_label.configure(image=scissor_comp_img)

    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    
    checkWin(x, compChoice)

def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose!")
            updateCompScore()
        else:
            updateMessage("You won!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lose!")
            updateCompScore()
        else:
            updateMessage("You won!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lose!")
            updateCompScore()
        else:
            updateMessage("You won!")
            updateUserScore()
    
    play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
    if not play_again:
        root.destroy()

root.mainloop()
