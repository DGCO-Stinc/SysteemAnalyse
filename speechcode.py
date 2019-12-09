from gtts import gTTS
from playsound import playsound

class Tts:
    
    def __init__(self):
        self.name = "henk"

    def speakit(self, text):
        v = gTTS(text=text, lang="nl", slow=False)
        v.save("name.mp3")
        playsound("name.mp3")
