import tkinter
from tkinter import ttk


presets = [1000, 250, 100, 10]

root = tkinter.Tk() #base window
root.title("clack")
root.resizable(width=False, height=False)

def cancel():
    print("cancel")

def confirm():
    newSpeed = int(speed.get())
    if (newSpeed == -1):
        print("custom mode caught! setting newSpeed to " + str(custom.get()) + "!")
        newSpeed = custom.get()
        
    print("confirming with speed " + str(newSpeed) + "!")

speed = tkinter.IntVar(name="speed") #this will be the variable modified by the radios and passed to the clicker module.
custom = tkinter.IntVar(name="custom") #value storage for custom speed input box.


baseFrame = tkinter.Frame(root).grid(row=0, column=0, columnspan=4, rowspan=5) #base frame around everything

bannerImg = tkinter.PhotoImage(file='banner.png')
titleCard = tkinter.Label(baseFrame, image=bannerImg).grid(  #logo at the top of the window
    column=0, row=0, columnspan=3, rowspan=3
)

instructions = tkinter.Label(baseFrame, text="Select a speed, given"
" in ms between clicks.").grid(column=0, row=3, columnspan=3, rowspan=1)



#the four preset radiobuttons
option0 = tkinter.Radiobutton(baseFrame, variable=speed, value=presets[0], text=presets[0], indicatoron=False).grid(column=4, row=0)
option1 = tkinter.Radiobutton(baseFrame, variable=speed, value=presets[1], text=presets[1], indicatoron=False).grid(column=4, row=1)
option2 = tkinter.Radiobutton(baseFrame, variable=speed, value=presets[2], text=presets[2], indicatoron=False).grid(column=4, row=2)
option3 = tkinter.Radiobutton(baseFrame, variable=speed, value=presets[3], text=presets[3], indicatoron=False).grid(column=4, row=3)

numInput = tkinter.Spinbox(baseFrame, textvariable=custom, increment=10, from_=10, to=100000).grid(column=2, row=5)

option4 = tkinter.Radiobutton(baseFrame, variable=speed, value=-1, text="custom", indicatoron=False).grid(column=4, row=5) #radiobutton for custom selector



acceptButton = tkinter.Button(text="confirm", command=confirm).grid(column=1, row=5)
cancelButton = tkinter.Button(text="cancel", command=cancel).grid(column=0, row=5)
# DELETE THIS AFTER FINISHING THE GUI
def main():
    root.mainloop()

main() 