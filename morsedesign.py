import tkinter as tk
from tkinter import Menu
import os
import sys
import morsebase

def morse_base():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','0','1','2','3','4','5','6','7','8','9', '\n']
    morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','/','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.', '\n']   
    uinput = userinput.get("1.0", 'end-1c')
    text4.delete('1.0', 'end')
    for char in uinput:
        converted = morse[alphabet.index(char).lower]
        text4.insert(tk.INSERT, converted)

#morse_base = morsebase.Converter()

#Preload
root = tk.Tk()
root.configure(bg="#dddddd")
root.title("MCC")

#Menu
menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)

menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=exit)

#Main Components
#Input
text1 = tk.Text(root, height=1, width=50) 
userinput = tk.Text(root, width=50, height=10)
#Output
text3 = tk.Text(root, height=1, width=50)
text4 = tk.Text(root, height=10, width=50)
#Buttons
b1 = tk.Button(root, text="To Morse", command=morse_base, bg="#dddddd", pady="4px", width="10")
b2 = tk.Button(root, text="To Text", bg="#dddddd", pady="4px", width="10")
#Speech Button
speaker = tk.PhotoImage(file="img/speaker_icon.png")
label = tk.Label(image=speaker)
#Input/Output Placeholder
text1.insert(tk.INSERT,"Input")
text3.insert(tk.INSERT,"Output")

#Styling Buttons
b1.config(relief="raised", bg="#bbbbbb")
b2.config(relief="raised", bg="#bbbbbb")

#disable input and output text
text1.config(state="disabled")
text3.config(state="disabled")
#text4.config(state="disabled")

#Exit Program 
def exit():
    root.quit()

#packs
#Input text
text1.pack()
#Input
userinput.pack()
#Output text
text3.pack()
#Output
text4.pack()
#Buttons
b1.pack(side=tk.LEFT, padx="1px", pady="1px")
b2.pack(side=tk.LEFT, padx="1px", pady="1px")
#Speaker image
label.pack(side=tk.RIGHT)

root.mainloop()
