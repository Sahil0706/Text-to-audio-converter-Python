from gtts import gTTS
import os

#myText = "Text To Speech Conversion Using Python"
fh=open("textdemo.txt","r")
myText=fh.read().replace("\n"," ")

language='en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")
fh.close()
os.system("start output.mp3")
