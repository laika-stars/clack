import tkinter
from tkinter import ttk


presets = [1000, 250, 100, 10]

root = tkinter.Tk() #base window
root.title("clack")
root.resizable(width=False, height=False)


speed = tkinter.IntVar() #this will be the variable modified by the radios and passed to the clicker module.
custom = tkinter.StringVar(value=1000) #value storage for custom speed input box. Must be string because of Entry widget.


baseFrame = tkinter.Frame(root, bg = "black") #base frame around everything

bannerImg = tkinter.PhotoImage(file='banner.png')
titleCard = tkinter.Label(baseFrame, image=bannerImg, bg="black") #logo at the top of the window

controlBox = tkinter.Frame(baseFrame, bg="black") #frame around all the controls

instructions = tkinter.Label(controlBox, text="Select a speed, given in ms between clicks.", bg="black", fg="white")

radioBox = tkinter.Frame(controlBox, bg="black") #frame around just the radio buttons for the speed controls

#the four preset radiobuttons
option0 = tkinter.Radiobutton(radioBox, variable=speed, value=presets[0], text=presets[0], bg="black", fg="grey", indicatoron=False)
option1 = tkinter.Radiobutton(radioBox, variable=speed, value=presets[1], text=presets[1], bg="black", fg="grey", indicatoron=False)
option2 = tkinter.Radiobutton(radioBox, variable=speed, value=presets[2], text=presets[2], bg="black", fg="grey", indicatoron=False)
option3 = tkinter.Radiobutton(radioBox, variable=speed, value=presets[3], text=presets[3], bg="black", fg="grey", indicatoron=False)

option4 = tkinter.Radiobutton(radioBox, variable=speed, value=custom, text="custom", bg="black", fg="grey", indicatoron=False) #radiobutton for custom selector

numInput = tkinter.Spinbox(radioBox, textvariable=custom, increment=10, from_=10, to=100000, bg="black", fg="white")

controlPanel = [option0, option1, option2, option3, option4, numInput]



titleCard.pack()
baseFrame.pack()
controlBox.pack()
instructions.pack()
radioBox.pack()
for control in controlPanel:
    control.pack()



# DELETE THIS AFTER FINISHING THE GUI
def main():
    root.mainloop()

main() 