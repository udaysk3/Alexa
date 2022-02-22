import wikipedia
import pyttsx3

engine = pyttsx3.init()

page  = wikipedia.summary('justin bieber',2,auto_suggest=False)
print(page)