import tkinter
import threading
from tkinter import ttk
from tkinter import *
import random
import datetime
import time
import math

def LeaderBoard():
    global leaderboard, cars

    bg2 = "#101010"
    fg2 = "orange"

    leaderboard = Tk()
    leaderboard.overrideredirect(1)
    leaderboard.title("Leaderboard")
    leaderboard.geometry("300x174+500+300")
    leaderboard.config(bg=bg2)
    ranking = []

    """
    font= "Segoe 10"
    font2= "Segoe 12 bold"
    """
    font = "Fixedsys 15"
    font2= "Fixedsys 20 bold"

    for x in range(0, len(cars)):
        for y in range(0, len(cars)):
            if cars[y][4] == x + 1:
                ranking.append([])
                ranking[x].append("Car No " + str(cars[y][0]))
                ranking[x].append(cars[y][3])

    #print(ranking)

    titleLabel = Label(leaderboard, text=" LEADERBOARD ", font=font2, background=bg2, foreground=fg2, anchor=CENTER , justify=CENTER)
    titleLabel.grid(row=0, column=0, columnspan=3, rowspan=1)

    for x in range(0, len(ranking)):
        no = Label(leaderboard, text="  " + str(x+1)+ "  ", font=font, background=bg2, foreground=fg2)
        no.grid(row=x+1, column=0, sticky="NSEW", rowspan=1, columnspan=2)

        if ranking[x][0] != "Car No 2" :
            car = Label(leaderboard, text=ranking[x][0], font=font, background=bg2, foreground=fg2, anchor=W)
            car.grid(row=x+1, column=2, sticky="NSEW", rowspan=1, columnspan=1)
        else:
            car = Label(leaderboard, text="You", font=font, background=bg2, foreground=fg2, anchor=W)
            car.grid(row=x+1, column=2, sticky="NSEW", rowspan=1, columnspan=1)

        carTimes = Label(leaderboard, text=ranking[x][1], font=font, background=bg2, foreground=fg2, anchor=W)
        carTimes.grid(row=x+1, column=3, sticky="NSEW", rowspan=1, columnspan=1)

    leaderboard.mainloop()


def move(event):
    if event.keysym.upper() == "M":
        if cars[1][1] < (.975*1250):
            xChange = random.randint(30, 35)
            gameCanvas.move(cars[1][0], xChange, 0)
            cars[1][1] += xChange

def clock():
    global timing
    timing = 0
    while pos != 6:
        time.sleep(0.01)
        timing += (0.02 * (10/7))
        timing = round(timing, 2)
        if pos != 1:
            timeLabel['text'] = timing        

def close():
    date = datetime.datetime.today()
    print("Closing file")
    file.destroy()
    try:
        leaderboard.destroy()
    except:
        pass

def play():
    global pos
    #initialTime = time.clock()
    #print(initialTime)

    while True:
        time.sleep(0.006)
        for car in cars:
            if car[1] < (.97*1250):
                if cars.index(car) != 1:
                    change = random.randint(1, 48)
                    change /= 10
                    gameCanvas.move(car[0], change, 0)
                    car[1] += change
                    #print(cars)
            if car[1] >= (.925*1250):
                if len(car) == 3:
                    pos += 1
                    timStr = str(round(timing, 2))
                    for x in range(0, len(timStr)):
                        if timStr[x] == ".":
                            break;

                    section = timStr[x+1:len(timStr)]
                    if len(section) == 1:
                        timStr + "0"


                    car.append(timStr)
                    car.append(pos)
            if pos == 6:
                LeaderBoard()
                break;

title="COUNTDOWN"
background="black"
background2= "gray"




title = "RACERS"
background = "black"
background2= "black"
foreground = "white"
bg2 = "#7A7A7A"
pos = 0

file = Tk()
file.title(title)
file.geometry("1250x650+10+50")
file.overrideredirect(1)
file.config(bg=background)

exitButton = Button(file, text= " × ", command = close, font="Arial 35", bd=0, background="black", foreground="white", cursor="hand2")
exitButton.config(activebackground=background, activeforeground="lightgray")
exitButton.place(relx=.95, rely=-.025)

fileTitle = Label(file, text=title, background=background, font="Segoe 29")
fileTitle.config(fg="white")
fileTitle.place(relx=.0, rely=.025)

gameCanvas = Canvas(file, width=1250, height=500, background=bg2, bd=0)
gameCanvas.place(relx=.0, rely=.1)

carsImages = ["racecar1.png", "racecar2.png", "racecar3.png", "racecar4.png", "racecar5.png", "racecar6.png"]
cars = []
photoImages = []

for c in carsImages:
    photoImage = PhotoImage(file=c)
    photoImages.append(photoImage)

for car in range(0, 6):
    xValue = 10
    yValue = (75*car) + 50
    car1 = gameCanvas.create_image(10, yValue, image=photoImages[car])
    cars.append([])
    cars[car].append(car1)
    cars[car].append(xValue)
    cars[car].append(yValue)

for car in range(0, 7):
    line = gameCanvas.create_line(0, (75*(car-1) + 90), 1250, (75*(car-1) + 90), width=3, fill="white")

#print(cars)

startLine = Canvas(gameCanvas, width=1, height=500)
startLine.place(relx=.05, rely=.0)

crossLine = Canvas(gameCanvas, width=1, height=500)
crossLine.place(relx=.975, rely=.0)

def countDown1():
    lbl.config(bg=background)
    lbl.config(foreground="white", font=('fixedsys 60'))
    for k in range(3, 0, -1):
        lbl["text"] = str(k)
        file.update()
        time.sleep(1)
    lbl.destroy()
    lbl2.destroy()

lbl = Label()
lbl.place(relx=.4, rely=.35)
lbl2 = Label(file, text="Press M to move the red car", font='fixedsys 15', bg=background)
lbl2.config(fg="white")
lbl2.place(relx=.32, rely=.49)
countDown1()

timeLabel = Label(file, text=0.000, font="Ebrima 20", width=10, anchor=E)
timeLabel.config(bg="white")
timeLabel.place(relx=.85, rely=.9)

file.bind("<KeyRelease>", move)

threading.Thread(target=play, args=()).start()
threading.Thread(target=clock, args=()).start()
threading.Thread(target=file.mainloop(), args=()).start()
