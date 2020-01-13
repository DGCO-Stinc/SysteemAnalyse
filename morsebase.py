class Converter:

    def __init__(self):
        # Alphabetical and morse code arrays
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','\n']
        self.morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.',
                      '---', '--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '/',
                      '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.','\n']
        self.name = "morty"

    def texttomorse(self, text):
        text = text.lower()
        converted = ""
        for char in text:
            converted += self.morse[self.alphabet.index(char)]
            converted += "/"
        return converted

    def morsetotext(self, morse):
        morse+=" "
        converted=""
        buffer = ""
        index = 0
        for char in morse:

            if char == ' ':
                converted += self.alphabet[self.morse.index(buffer)]
                buffer = ""
            elif char == "." or char == "-" or char == "/":
                buffer += char
            elif index == len(morse):
                buffer += char
                converted += self.alphabet[self.morse.index(buffer)]
                #return converted
            else:
                print("Error: input unexpected")
                break
            index += 1
        return converted
