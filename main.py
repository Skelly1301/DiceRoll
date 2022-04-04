import tkinter
import tkinter.messagebox
import random

window = tkinter.Tk()
window.geometry('240x240')

min = 1
max = 6

def diceResult():
    diceOutput = str(random.randint(min,max))
    print(' Dice Value ', diceOutput) 
    button['text']= 'Dice Rolled' + diceOutput
    imageFile = "images/Dice"+diceOutput+".png"
    window.photo1 = tkinter.PhotoImage(file = imageFile )
    button['image'] = window.photo1

button = tkinter.Button(window, text="Click to roll the dice" , command= diceResult)
button.pack()
window.title('Digital Dice')
window.mainloop()
