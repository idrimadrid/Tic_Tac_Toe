from tkinter import *
from tkinter import messagebox


def nextRound():
    global player
    global round
    round += 1
    if (player == 1):
        player = 2
    else:
        player = 1


def win():
    global btn_list
    global scorex, scoreo
    # lignes
    if (btn1.cget('text') == "o" and btn2.cget('text') == btn1.cget('text') and btn2.cget('text') == btn3.cget(
            'text') or btn4.cget('text') == "o" and btn5.cget('text') == btn4.cget('text') and btn5.cget(
        'text') == btn6.cget('text') or btn7.cget('text') == "o" and btn8.cget('text') == btn7.cget(
        'text') and btn8.cget('text') == btn9.cget('text')):
        messagebox.showinfo("Partie Terminer", "O won")
        scoreo += 1
        if (messagebox.askquestion("Rejouer", "Voulez Vous Rejouer ?")):
            reset(btn_list)
    elif (btn1.cget('text') == "x" and btn2.cget('text') == btn1.cget('text') and btn2.cget('text') == btn3.cget(
            'text') or btn4.cget('text') == "x" and btn5.cget('text') == btn4.cget('text') and btn5.cget(
        'text') == btn6.cget('text') or btn7.cget('text') == "x" and btn8.cget('text') == btn7.cget(
        'text') and btn8.cget('text') == btn9.cget('text')):
        messagebox.showinfo("Partie Terminer", "X won")
        scorex += 1
        if (messagebox.askquestion("Rejouer", "Voulez Vous Rejouer ?")):
            reset(btn_list)
        # colonnes
    elif (btn1.cget('text') == "x" and btn4.cget('text') == btn1.cget('text') and btn4.cget('text') == btn7.cget(
            'text') or btn2.cget('text') == "x" and btn5.cget('text') == btn2.cget('text') and btn5.cget(
        'text') == btn8.cget('text') or btn3.cget('text') == "x" and btn3.cget('text') == btn9.cget(
        'text') and btn6.cget('text') == btn9.cget('text')):
        messagebox.showinfo("Partie Terminer", "X won")
        scorex += 1
        if (messagebox.askquestion("Rejouer", "Voulez Vous Rejouer ?")):
            reset(btn_list)
    elif (btn1.cget('text') == "o" and btn4.cget('text') == btn1.cget('text') and btn4.cget('text') == btn7.cget(
            'text') or btn2.cget('text') == "o" and btn5.cget('text') == btn2.cget('text') and btn5.cget(
        'text') == btn8.cget('text') or btn3.cget('text') == "o" and btn3.cget('text') == btn9.cget(
        'text') and btn6.cget('text') == btn9.cget('text')):
        messagebox.showinfo("Partie Terminer", "O won")
        scoreo += 1
        if (messagebox.askquestion("Rejouer", "Voulez Vous Rejouer ?")):
            reset(btn_list)
    # Diags
    elif (btn1.cget('text') == "o" and btn5.cget('text') == btn1.cget('text') and btn5.cget('text') == btn9.cget(
            'text') or btn3.cget('text') == "o" and btn5.cget('text') == btn3.cget('text') and btn5.cget(
        'text') == btn7.cget('text')):
        messagebox.showinfo("Partie Terminer", "O won")
        scoreo += 1
        if (messagebox.askquestion("Rejouer", "Voulez Vous Rejouer ?")):
            reset(btn_list)
    elif (btn1.cget('text') == "x" and btn5.cget('text') == btn1.cget('text') and btn5.cget('text') == btn9.cget(
            'text') or btn3.cget('text') == "x" and btn5.cget('text') == btn3.cget('text') and btn5.cget(
        'text') == btn7.cget('text')):
        messagebox.showinfo("Partie Terminer", "X won")
        scorex += 1
        if (messagebox.askquestion("Rejouer", "Voulez Vous Rejouer ?")):
            reset(btn_list)
    elif (round == 9):
        messagebox.showinfo("Partie Terminer", "Tie")
        if (messagebox.askquestion("Rejouer", "Voulez Vous Rejouer ?")):
            reset(btn_list)
    update_score()


def addimg(btn):
    if (player == 1):
        btn.config(text="o", image=po, width=0, height=0)
    else:
        btn.config(text="x", image=px, width=0, height=0)
    btn.config(state=DISABLED)
    nextRound()
    win()


def reset(list):
    global round
    for btn in list:
        btn.config(text="", image='', state=NORMAL, width=25, height=12)
    round = 0


def update_score():
    global btn11
    global btn12
    btn11.config(text="Score de X : " + str(scorex))
    btn12.config(text="Score de O : " + str(scoreo))


main = Tk()
main.geometry('650x600')
main.resizable(0, 0)
main.title("Tic Tac Toe")
player = 1
round = 0
scorex = 0
scoreo = 0
# import photos
po = PhotoImage(file="O.png")
px = PhotoImage(file="X.png")
#  Creation Buttons
btn_list = []
btn1 = Button(main, text="", width=25, height=12, command=lambda: addimg(btn1))
btn_list.append(btn1)
btn1.grid(row=0, column=0)
btn2 = Button(main, text="", width=25, height=12, command=lambda: addimg(btn2))
btn_list.append(btn2)
btn2.grid(row=0, column=1)
btn3 = Button(main, text="", width=25, height=12, command=lambda: addimg(btn3))
btn_list.append(btn3)
btn3.grid(row=0, column=2)
btn4 = Button(main, text="", width=25, height=12, command=lambda: addimg(btn4))
btn_list.append(btn4)
btn4.grid(row=1, column=0)
btn5 = Button(main, text="", width=25, height=12, command=lambda: addimg(btn5))
btn_list.append(btn5)
btn5.grid(row=1, column=1)
btn6 = Button(main, text="", width=25, height=12, command=lambda: addimg(btn6))
btn_list.append(btn6)
btn6.grid(row=1, column=2)
btn7 = Button(main, text="", width=25, height=12, command=lambda: addimg(btn7))
btn_list.append(btn7)
btn7.grid(row=2, column=0)
btn8 = Button(main, text="", width=25, height=12, command=lambda: addimg(btn8))
btn_list.append(btn8)
btn8.grid(row=2, column=1)
btn9 = Button(main, text="", width=25, height=12, command=lambda: addimg(btn9))
btn_list.append(btn9)
btn9.grid(row=2, column=2)
btn10 = Button(main, text="Rejouer", command=lambda: reset(btn_list))
btn10.grid(row=1, column=3)
btn11 = Label(main, text="Score de X : " + str(scorex))
btn11.grid(row=0, column=3)
btn12 = Label(main, text="Score de O : " + str(scoreo))
btn12.grid(row=2, column=3)
main.mainloop()
