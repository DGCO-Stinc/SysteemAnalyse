import sys
sys.path.append('..')
import morsebase

converter = morsebase.Converter()

morse = input("Morse:\n")
converter.morsetotext(morse)

#where is this file?