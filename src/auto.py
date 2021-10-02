import random, threading
from time import sleep
from PySimpleGUI.PySimpleGUI import Button
import pyautogui
import pydirectinput #Like pyautogui but uses the SendInput https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendinput
import pygetwindow as gw
from tkinter import * # pylint: disable=unused-wildcard-import 

start_stop=1

def press_random_wasd(args):
    #Generate which button to press
    
    
    if (args == "start"):
        val = random.choice(["W","A","S","D"])
        pyautogui.press(val) #press it
        time_out_time = random.randint(1,60) #Generate timeout time
        sleep(time_out_time)

    if (args == "long"):
        val = random.choice(["W","A","S","D"])
        pyautogui.press(val) #press it
        time_out_time = random.randint(600,1140) #Generate timeout time
        sleep(time_out_time)
    
    if (args == "start_SendInput"):
        val = random.choice(["W","A","S","D"])
        pydirectinput.press(val) #press it
        time_out_time = random.randint(1,60) #Generate timeout time
        sleep(time_out_time)

    if (args == "long_SendInput"):
        val = random.choice(["W","A","S","D"])
        pydirectinput.press(val) #press it
        time_out_time = random.randint(600,1140) #Generate timeout time
        sleep(time_out_time)

    return


## On state function
def main_anti_afk(args):
    start_btn["state"] = "disabled"
    start_btn.config(cursor="watch")
    start_btn_long["state"] = "disabled"
    start_btn_long.config(cursor="watch") 

    start_btn_SendInput["state"] = "disabled"
    start_btn_SendInput.config(cursor="watch")
    start_btn_long_SendInput["state"] = "disabled"
    start_btn_long_SendInput.config(cursor="watch") 

    while (start_stop==1):
        press_random_wasd(args)

        
    start_btn["state"] = "normal"
    start_btn.config(cursor="arrow") #Change back to the normal mouse cursor when it's hovering over
    start_btn_long["state"] = "normal"
    start_btn_long.config(cursor="arrow")
    start_btn_SendInput["state"] = "normal"
    start_btn_SendInput.config(cursor="arrow")
    start_btn_long_SendInput["state"] = "normal"
    start_btn_long_SendInput.config(cursor="arrow")


def start_up_process(arguments):
    threading.Thread(target=main_anti_afk, args=[arguments]).start()
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


root.minsize( 350, 100) #minimum window size
root.geometry("350x100") #Window start up size

start_btn = Button( root, text="Start", command=lambda: start_up_process("start"))
start_btn.grid(row=0, column=0)

start_btn_long = Button( root, text="Start slow timmer", command=lambda: start_up_process("long"))
start_btn_long.grid(row=0, column=1)

start_btn_SendInput = Button( root, text="Start with SendInput ", command=lambda: start_up_process("start_SendInput"))
start_btn_SendInput.grid(row=1, column=0)

start_btn_long_SendInput = Button( root, text="Start slow timmer with SendInput", command=lambda: start_up_process("long_SendInput"))
start_btn_long_SendInput.grid(row=1, column=1)

stop_btn = Button( root, text="Stop", command=stop_process)
stop_btn.grid(row=2, column=0)

root.mainloop()