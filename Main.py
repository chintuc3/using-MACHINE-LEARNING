from tkinter import messagebox
from tkinter import *
import tkinter
from spellchecker import SpellChecker

main = Tk()
main.title("Auto Correction")
main.geometry("600x500")

spell = SpellChecker()
global word1, word2, word3

def correction():
    tf2.delete(0, 'end')
    global word1, word2, word3
    word1 = ""
    word2 = ""
    word3 = ""
    l3.config(text="")
    l4.config(text="")
    l5.config(text="")
    word = tf1.get()
    word = word.split()
    misspelled = spell.unknown(word)
    for word in misspelled:
        tf2.insert(0, str(spell.correction(word)))
        candidate = spell.candidates(word)
        if candidate is not None:
            candidate = list(candidate)
            print(candidate)
            print(type(candidate))
            if len(candidate) > 0:
                l3.config(text=candidate[0])
                word1 = candidate[0]
            if len(candidate) > 1:
                l4.config(text=candidate[1])
                word2 = candidate[1]
            if len(candidate) > 2:
                l5.config(text=candidate[2])
                word3 = candidate[2]

def setFirst(event):
    tf2.delete(0, 'end')
    tf2.insert(0, str(word1))      

def setSecond(event):
    tf2.delete(0, 'end')
    tf2.insert(0, str(word2))

def setThird(event):
    tf2.delete(0, 'end')
    tf2.insert(0, str(word3))    

def clear():
    tf1.delete(0, 'end')
    tf2.delete(0, 'end')
    l3.config(text="")
    l4.config(text="")
    l5.config(text="")
    
font = ('times', 18, 'bold')
title = Label(main, text='Auto Correction')
title.config(bg='mint cream', fg='olive drab')  
title.config(font=font)           
title.place(x=150,y=30)

font1 = ('times', 13, 'bold')

l1 = Label(main, text='         Input Word:')
l1.config(font=font1)
l1.place(x=50,y=100)

tf1 = Entry(main,width=30)
tf1.config(font=font1)
tf1.place(x=210,y=100)

runButton = Button(main, text="Correction", command=correction)
runButton.place(x=180,y=150)
runButton.config(font=font1)

l2 = Label(main, text='Corrected Word:')
l2.config(font=font1)
l2.place(x=50,y=200)

tf2 = Entry(main,width=30)
tf2.config(font=font1)
tf2.place(x=210,y=200)

uploadButton = Button(main, text="Clear", command=clear)
uploadButton.place(x=180,y=250)
uploadButton.config(font=font1)


l3 = Label(main, text='')
l3.config(font=font1)
l3.place(x=50,y=300)
l3.bind("<1>", setFirst)

l4 = Label(main, text='')
l4.config(font=font1)
l4.place(x=250,y=300)
l4.bind("<1>", setSecond)

l5 = Label(main, text='')
l5.config(font=font1)
l5.place(x=450,y=300)
l5.bind("<1>", setThird)

main.config(bg='chocolate1')
main.mainloop()
