import sys
sys.path.append('..')
import morsebase

converter = morsebase.Converter()

text = input("word please\n>")
converter.texttomorse(text)
