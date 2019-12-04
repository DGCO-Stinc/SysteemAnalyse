
class Converter:

    def __init__(self):
        #Alphabetical and morse code arrays
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','0','1','2','3','4','5','6','7','8','9']
        self.morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','/','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
        self.name = "morty"

    def texttomorse(self,text):
        for char in text:
            converted = self.morse[self.alphabet.index(char)]
            print(converted, end=' ')

    def morsetotext(self,morse):
        for char in morse:
            converted = self.alphabet[self.morse.index(char)]
            print(converted, end=' ')
        