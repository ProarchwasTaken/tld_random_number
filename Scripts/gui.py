import tkinter
from engine import *

window = tkinter.Tk()
rResult = 0
minNum_var = tkinter.StringVar()
maxNum_var = tkinter.StringVar()

def calculate():

    print("INFO: The calculate button has been pressed.")

    minNum = minNum_var.get()
    maxNum = maxNum_var.get()
    #If one of the text entered into the entry boxes, nothing will happen
    
    rResult = random.randint(int(minNum), int(maxNum))
    rResult = round(rResult)
    resultNUM.config(text=rResult)
    print("DEBUG: ",rResult)

# Displays the greet text.
greetText = tkinter.Label(window, text= "Welcome to my \nrandom number generator!", fg="blue", font=("Arial", 16))
greetText.place(placeGT.objectData)

# Displays the help text.
helpText = tkinter.Label(window, text= "Just enter a WHOLE number in each of those boxes, \nclick calculate and the program will guess a random \nnumber between the numbers you selected")
helpText.place(placeHT.objectData)

# Displays the credit text
credits = tkinter.Label(window, text= 'Program made by: Tyler "Proarch" 2022', font=("Arial", 8))
credits.place(placeCT.objectData)

# Displays result number. This one is special
resultNUM = tkinter.Label(window, text= "0", fg="red", font=("Arial", 20))
resultNUM.place(placeRN.objectData)

#Displays less than symbol
lessSymbol = tkinter.Label(window, text= '<', font=("Arial", 20))
lessSymbol.place(placeLS.objectData)

# Displays Calculate Button
calButton = tkinter.Button(window, text= "Calculate", command=calculate)
calButton.place(placeCB.objectData)

# Creates 2 Entry Boxes
minfld = tkinter.Entry(window, textvariable = minNum_var,bd=5, width=10)
minfld.place(placeminIE.objectData)

maxfld = tkinter.Entry(window, textvariable = maxNum_var, bd=5, width=10)
maxfld.place(placemaxIE.objectData)

window.title("RN Generator by Tyler")

window.geometry("300x275")


window.mainloop()