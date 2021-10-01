import random
from time import sleep
import pyautogui
import pygetwindow as gw
import PySimpleGUI as sg



def press_random_wasd():
    #Generate which button to press
    val = random.choice(["W","A","S","D"])
    pyautogui.press(val) #press it
    time_out_time = random.randint(1,60) #Generate timeout time
    sleep(time_out_time)
    return




## Main loop of the program
def main():
    x=1
    while (x==1):
        if (gw.getActiveWindow().title == "New World"): #Check if new world is open else wait 20s and check again
            press_random_wasd()
        else:
            sleep(20)

    


if __name__ == "__main__":
    main()