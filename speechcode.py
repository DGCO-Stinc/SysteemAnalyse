from gtts import gTTS
from playsound import playsound

class Tts:
    
    def __init__(self):
        self.name = "henk"
        self.count = 0

    def speakit(self, text):
        
        v = gTTS(text=text, lang="nl", slow=False)
        v.save(f"name{self.count%10}.mp3")
        playsound(f"name{self.count%10}.mp3")
        self.count += 1