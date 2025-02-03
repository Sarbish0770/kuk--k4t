from gtts import gTTS
from datetime import date
import os

language = 'en'
today = date.today()
date_string = today.strftime("%A %B %D")  # Format today's date

text = f"Hello sir, I am Friday. for your kind" 
text1  = f"Today is {date_string}."
tts = gTTS(text=text+text1, lang=language, slow=False)
tts.save("output.mp3")
os.system("play output.mp3")


