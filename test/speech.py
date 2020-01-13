import sys
sys.path.append("..")
import speechcode

tts = speechcode.Tts()



while(True):
    text = input("zegeensiets\n")
    if text=="e":
        break
    else:
        tts.speakit(text)