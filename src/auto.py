import random, threading
from time import sleep
from PySimpleGUI.PySimpleGUI import Button
import pyautogui
import pygetwindow as gw
from tkinter import * # pylint: disable=unused-wildcard-import 

start_stop=1

def press_random_wasd():
    #Generate which button to press
    val = random.choice(["W","A","S","D"])
    pyautogui.press(val) #press it
    time_out_time = random.randint(1,60) #Generate timeout time
    sleep(time_out_time)
    return


## On state function
def main_anti_afk():
    while (start_stop==1):
        start_btn["state"] = "disabled"
        start_btn.config(cursor="watch") 
        if (gw.getActiveWindow().title == "New World"): #Check if new world is open else wait 20s and check again
            press_random_wasd()
        else:
            sleep(20)
    start_btn["state"] = "normal"
    start_btn.config(cursor="arrow") #Change back to the normal mouse cursor when it's hovering over


def start_up_process():
    threading.Thread(target=main_anti_afk).start()
    return


def main_stop():
    global start_stop
    start_stop=0

def stop_process():
    threading.Thread(target=main_stop).start()

##GUI Code bellow

#TK set up
root = Tk()
root.title(" Auto-AFK-clicker") #Title/Name of program in top bar


root.minsize( 150, 100) #minimum window size
root.geometry("150x100") #Window start up size

start_btn = Button( root, text="Start", command=start_up_process)
start_btn.grid(row=0, column=0)

stop_btn = Button( root, text="Stop", command=stop_process)
stop_btn.grid(row=0, column=1)

root.mainloop()