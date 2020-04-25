#New Program

import random
from tkinter import *
def countersInc(event):

    global varSuccess,varMissed
    if(event.widget["bg"]=="red"):
        varSuccess.set(varSuccess.get()+1)
    else:
        varMissed.set(varMissed.get()+1)

def createGameButtons():
    btnNo=0
    for i in range(1,5):
        for j in range(4):
            btnNo+=1
            btnGame=Button(root,text="%d"%btnNo,height=3,width=8)
            btnGame.bind("<Button 1>",countersInc)
            btnGame.grid(row=i,column=j)

def createotherWidgets():
    lblSuccess=Label(root,text="Success",height=3)
    lblSuccess.grid(row=0,column=0)
    global varSuccess
    varSuccess=IntVar()
    entrySuccess=Entry(root,textvariable=varSuccess,width=6)
    entrySuccess.grid(row=0, column=1)

    lblMissed = Label(root, text="Missed", height=3)
    lblMissed.grid(row=0, column=2)
    global varMissed
    varMissed = IntVar()
    entryMissed = Entry(root, textvariable=varMissed, width=6)
    entryMissed.grid(row=0, column=3)

    btnStart=Button(root,text="Start",command=btnStart_Click,width=8,height=3)
    btnStart.grid(row=5,column=1)

    btnStop = Button(root, text="Stop",command=btnStop_Click,width=8,height=3)
    btnStop.grid(row=5, column=2)

def btnStart_Click():
    global startstop
    startstop=1
    startGame()

def btnStop_Click():
    global startstop
    startstop = 0
    startGame()

def startGame():
    global redBtn,startstop
    if(startstop==0):
        return
    else:
        if(redBtn==0):
            pass
        else:
            redBtn["bg"] = "white"

        varRandomRow=random.randint(1,4)
        varRandomColumn=random.randint(0,3)
        randomGameBtnList=root.grid_slaves(row=varRandomRow,column=varRandomColumn)
        redBtn=randomGameBtnList[0]
        redBtn["bg"]="red"
        root.after(1000,startGame)

root=Tk()

createGameButtons()
createotherWidgets()
redBtn=0
startstop=0

root.mainloop()