import mouse #used to click the mouse
import threading #used to create separate threads for the clicker so it isnt in the same thread as the keystroke detector
import keyboard #used to detect keystrokes to start and stop the program.
import sys #used to exit in errored states and report the error.
import time #used to sleep between clicks.

latch = threading.Event #we shall use this to toggle clicks.

global speed; speed = 1000 #global of how much to delay.
global type; type = 0 #global of what click to click.

'''
this is its own function so that we can use different clicks easily.
just add another case with a new number.
type = int: the type of click, selected from the below options.
0: left click
1: right click
'''
def click(type: int = 0):
    match type:
        case 0:
            mouse.click()
        case 1:
            mouse.right_click()
        case _: #this is the default/fallback case
            sys.exit('ERROR: undefined click type "' + type + '".') #complain

'''
Mashes click() with the specified delay.
'''
def clickLoop(): 
    while (latch.wait()):
        click(type) #click that type
        time.sleep(speed) # wait that long

thread = threading.Thread(target=clickLoop)

def initialise():
    thread.start()

def startClicking(delay, clickType: int = 0):
    speed = delay #copy param to global
    type = clickType #copy param to global
    latch.set() # its GO time !!!
    print("started clicking boss")

def stopClicking():
    latch.clear() #its GO'N'T time !!

