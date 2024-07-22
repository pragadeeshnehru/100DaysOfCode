import tkinter
import tkinter.messagebox
import random
from PIL import Image, ImageTk

window = tkinter.Tk()
window.geometry('240x240')

min = 1
max = 6

def diceResult():
    diceOutput = str(random.randint(min, max))
    print(' Dice Value ', diceOutput)
    button['text'] = 'Dice Rolled ' + diceOutput

    # Modify path to absolute when running locally
    imageFile = f"Dice{diceOutput}.png"
    
    img = Image.open(imageFile)
    img = img.resize((240, 240), Image.LANCZOS)
    window.photo1 = ImageTk.PhotoImage(img)
    button['image'] = window.photo1

button = tkinter.Button(window, text="Click to roll the dice", command=diceResult)
button.pack()
window.title('Digital Dice')
window.mainloop()
