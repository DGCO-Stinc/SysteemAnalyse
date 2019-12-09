import tkinter as tk
import morsebase

def morse_base():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','0','1','2','3','4','5','6','7','8','9']
    morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','/','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']   
    text = text2.get()
    text4.delete('1.0', 'end')
    for char in text:
        converted = morse[alphabet.index(char)]
        text4.insert(tk.INSERT, converted)


class Window:

    def __init__(self):
        self.mc = morsebase.Converter()
        self.root = tk.Tk()
        self.root.title("MortyCodeConverter")
        self.text1 = tk.Text(self.root,height=1,width=50)
        self.text2 = tk.Entry(self.root, width=50)
        self.text3 = tk.Text(self.root, height=1, width=50)
        self.text4 = tk.Text(self.root, height=10, width=50)
        self.b1 = tk.Button(self.root, text="To morse", command=self.ttm(self.text2))
        self.b2 = tk.Button(self.root, text="To text")
        self.speaker = tk.PhotoImage(file="img/speaker_icon.png")
        self.label = tk.Label(image=self.speaker)
        self.text1.insert(tk.INSERT,"Input")
        self.text3.insert(tk.INSERT,"Output")
        #packs
        #Input text
        self.text1.pack()
        #Input
        self.text2.pack()
        #Speaker image
        self.label.pack()
        #Output text
        self.text3.pack()
        #Output
        self.text4.pack()
        #Buttons
        self.b1.pack(side=tk.LEFT)
        self.b2.pack(side=tk.LEFT)
        
        #disable input and output text
        self.text1.config(state="disabled")
        self.text3.config(state="disabled")
        #text4.config(state="disabled")
        self.root.mainloop()

    def ttm(self, text):
        input = str(self.text1.get("1.0",'end'))
        self.mc.texttomorse(input)



# root = tk.Tk()
# root.title("Morse")
# text1 = tk.Text(root, height=1, width=50)
# text2 = tk.Entry(root, width=50)
# text3 = tk.Text(root, height=1, width=50)
# text4 = tk.Text(root, height=10, width=50)
# b1 = tk.Button(root, text="To morse", command=mc.texttomorse(text2))
# b2 = tk.Button(root, text="To text")
# speaker = tk.PhotoImage(file="img/speaker_icon.png")
# label = tk.Label(image=speaker)
# text1.insert(tk.INSERT,"Input")
# text3.insert(tk.INSERT,"Output")


# #disable input and output text
# text1.config(state="disabled")
# text3.config(state="disabled")
# #text4.config(state="disabled")

# #packs
# #Input text
# text1.pack()
# #Input
# text2.pack()
# #Speaker image
# label.pack()
# #Output text
# text3.pack()
# #Output
# text4.pack()
# #Buttons
# b1.pack(side=tk.LEFT)
# b2.pack(side=tk.LEFT)

# root.mainloop()

mainframe = Window()