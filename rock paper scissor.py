from tkinter import *
import random
import pygame
from PIL import ImageTk, Image

user_score = 0
computer_score = 0

root = Tk()
root.geometry('610x500')
root.title("Rock Paper Scissor Game-Shubham Pathak")
root.configure(bg="#85ffdd")

pygame.mixer.init()


def click_rock():
    rock_paper_scissor = ['Rock', 'Paper', 'Scissors']
    computer_choose = random.choice(rock_paper_scissor)

    global user_score
    global computer_score

    if computer_choose == "Rock":
        user_score += 0
        computer_score += 0
        result.configure(text="DRAW")
    if computer_choose == "Paper":
        user_score += 0
        computer_score += 1
        pygame.mixer.music.load(r'looser.mp3')
        pygame.mixer.music.play()
        result.configure(text="LOSS")
    if computer_choose == "Scissors":
        user_score += 1
        computer_score += 0
        pygame.mixer.music.load(r'winner.mp3')
        pygame.mixer.music.play()
        result.configure(text="WIN")

    computer_chose.configure(text=computer_choose, fg="red")
    user_score_label.configure(text=user_score, bg="yellow", fg="red")
    computer_score_label.configure(text=computer_score, bg="yellow", fg="red")

def click_paper():
    rock_paper_scissor = ['Rock', 'Paper', 'Scissors']
    computer_choose = random.choice(rock_paper_scissor)
    global user_score
    global computer_score

    if computer_choose == "Rock":
        user_score += 1
        computer_score += 0
        pygame.mixer.music.load(r'winner.mp3')
        pygame.mixer.music.play()
        result.configure(text="WIN")
    if computer_choose == "Paper":
        user_score += 0
        computer_score += 0
        result.configure(text="DRAW")
    if computer_choose == "Scissors":
        user_score += 0
        computer_score += 1
        pygame.mixer.music.load(r'looser.mp3')
        pygame.mixer.music.play()
        result.configure(text="LOSS")

    computer_chose.configure(text=computer_choose, fg="red")
    user_score_label.configure(text=user_score, bg="yellow", fg="red")
    computer_score_label.configure(text=computer_score, bg="yellow", fg="red")

def click_scissor():
    rock_paper_scissor = ['Rock', 'Paper', 'Scissors']
    computer_choose = random.choice(rock_paper_scissor)
    global user_score
    global computer_score

    if computer_choose == "Rock":
        user_score += 0
        computer_score += 1
        pygame.mixer.music.load(r'looser.mp3')
        pygame.mixer.music.play()
        result.configure(text="LOSS")
    if computer_choose == "Paper":
        user_score += 1
        computer_score += 0
        pygame.mixer.music.load(r'winner.mp3')
        pygame.mixer.music.play()
        result.configure(text="WIN")
    if computer_choose == "Scissors":
        user_score += 0
        computer_score += 0
        result.configure(text="DRAW")
        
    computer_chose.configure(text=computer_choose, fg="red")
    user_score_label.configure(text=user_score, bg="yellow", fg="red")
    computer_score_label.configure(text=computer_score, bg="yellow", fg="red")

def end_game():
    rock.destroy()
    paper.destroy()
    scissor.destroy()
    compchosen.destroy()
    computer_chose.destroy()
    your.destroy()
    user_score_label.destroy()
    comp.destroy()
    computer_score_label.destroy()
    end.destroy()
    rockLbl.destroy()
    scissorLbl.destroy()
    paperLbl.destroy()
    notice_comp.destroy()
    notice_your.destroy()
    result.destroy()
    root.configure(bg="#cc92ba")

    Label(root, text=f"Your Score was  {user_score}", bg="#CC92BA", font="Algerian 25 bold").place(x=120, y=100)
    Label(root, text=f"Computer's Score was  {computer_score}", bg="#CC92BA", font="Algerian 25 bold").place(x=70, y=350)

    if user_score > computer_score:
        Label(root, text="YOU WON", font="helvatica 50 bold", fg="red", bg="#cc92ba").place(x=100, y=200)
        pygame.mixer.music.load(r'final win.mp3')
        pygame.mixer.music.play()

    if user_score < computer_score:
        Label(root, text="YOU LOSE", font="helvatica 50 bold", fg="red", bg="#cc92ba").place(x=100, y=200)
        pygame.mixer.music.load(r'final loss.mp3')
        pygame.mixer.music.play()

    if user_score == computer_score:
        Label(root, text="DRAW", font="helvatica 50 bold", fg="red", bg="#cc92ba").place(x=165, y=200)

def button_enter_rock(event):
    rock.configure(bg="blue")
def button_enter_paper(event):
    paper.configure(bg="blue")
def button_enter_scissor(event):
    scissor.configure(bg="blue")
def end_enter(event):
    end.configure(bg="gray")
def user_score_enter(event):
    notice_your.configure(text="Your Score", bg="white")
def comp_score_enter(event):
    notice_comp.configure(text="Computer's Score", bg="white")

def button_leave_rock(event):
    rock.configure(bg="yellow")
def button_leave_paper(event):
    paper.configure(bg="yellow")
def button_leave_scissor(event):
    scissor.configure(bg="yellow")
def end_leave(event):
    end.configure(bg="pink")
def user_score_leave(event):
    notice_your.configure(text="", bg="#85ffdd")
def comp_score_leave(event):
    notice_comp.configure(text="", bg="#85ffdd")

# Images
paperImg = ImageTk.PhotoImage(Image.open(r'Paper.png'))
rockImg = ImageTk.PhotoImage(Image.open(r'Rock.png'))
scissorsImg = ImageTk.PhotoImage(Image.open(r'Scissors.png'))
userImg = ImageTk.PhotoImage(Image.open(r'user.png'))
compImg = ImageTk.PhotoImage(Image.open(r'computer.png'))

rock = Button(root, image=rockImg, text="ROCK", command=click_rock, bg="yellow")
rock.place(x=30, y=70)
rock.bind("<Enter>", button_enter_rock)
rock.bind("<Leave>", button_leave_rock)
rockLbl = Label(root, text="Rock", font="Algerian 15 bold", bg="#85ffdd")
rockLbl.place(x=72, y=227)

paper = Button(root, image=paperImg, text="PAPER", command=click_paper, bg="yellow")
paper.place(x=235, y=70)
paper.bind("<Enter>", button_enter_paper)
paper.bind("<Leave>", button_leave_paper)
paperLbl = Label(root, text="Paper", font="Algerian 15 bold", bg='#85ffdd')
paperLbl.place(x=252, y=227)

scissor = Button(root, image=scissorsImg, text="SCISSOR", command=click_scissor, bg="yellow")
scissor.place(x=400, y=70)
scissor.bind("<Enter>", button_enter_scissor)
scissor.bind("<Leave>", button_leave_scissor)
scissorLbl = Label(root, text="Scissors", font="Algerian 15 bold", bg="#85ffdd")
scissorLbl.place(x=450, y=227)

compchosen = Label(root, text="Computer Chose:- ", font="helvatica 15", bg="#85ffdd")
compchosen.place(x=170, y=305)
computer_chose = Label(root, text="None", font="helvatica 15 bold", bg="#85ffdd")
computer_chose.place(x=330, y=305)

your = Label(root, text="Your Score = ", image=userImg, bg="#85ffdd")
your.place(x=50, y=400)
your.bind("<Enter>", user_score_enter)
your.bind("<Leave>", user_score_leave)
notice_your = Label(root, bg="#85ffdd")
notice_your.place(x=30, y=405)
user_score_label = Label(root, text="", font="helvatica 25 bold", bg="red")
user_score_label.place(x=105, y=400)

comp = Label(root, text="Computer Score = ", image=compImg, bg="#85ffdd")
comp.place(x=440, y=400)
comp.bind("<Enter>", comp_score_enter)
comp.bind("<Leave>", comp_score_leave)
notice_comp = Label(root, bg="#85ffdd")
notice_comp.place(x=400, y=405)
computer_score_label = Label(root, text="", font="helvatica 25 bold", bg="red")
computer_score_label.place(x=505, y=400)

result = Label(root, font="helvatica 25 bold", fg="blue", bg="#85ffdd")
result.place(x=250, y=20)

end = Button(root, text='END Game', command= end_game, bg="pink", fg="blue", padx=10, font="Algerian 10")
end.place(x=250, y=450)
end.bind("<Enter>", end_enter)
end.bind("<Leave>", end_leave)

root.mainloop()