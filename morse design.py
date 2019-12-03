import tkinter as tk

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
morse = ['.-','-...','-.-.-','-..','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']


root = tk.Tk()
root.title("Morse")
text1 = tk.Text(root, height=1, width=50)
text2 = tk.Text(root, height=10, width=50)
text3 = tk.Text(root, height=1, width=50)
text4 = tk.Text(root, height=10, width=50)
b1 = tk.Button(root, text="To morse")
b2 = tk.Button(root, text="To text")
speaker = tk.PhotoImage(file="img/speaker_icon.png")
label = tk.Label(image=speaker)
text1.insert(tk.INSERT,"Input")
text3.insert(tk.INSERT,"Output")

#disable input and output text
text1.config(state="disabled")
text3.config(state="disabled")
text4.config(state="disabled")


#packs
#Input text
text1.pack()
#Input
text2.pack()
#Speaker image
label.pack()
#Output text
text3.pack()
#Output
text4.pack()
#Buttons
b1.pack(side=tk.LEFT)
b2.pack(side=tk.LEFT)

root.mainloop()