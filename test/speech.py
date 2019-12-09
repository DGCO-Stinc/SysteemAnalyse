import sys
sys.path.append("..")
import speechcode

tts = speechcode.Tts()

text = input("zegeensiets\n")

tts.speakit(text)