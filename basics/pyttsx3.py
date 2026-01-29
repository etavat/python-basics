import pyttsx3
import pyjokes
joke = pyjokes.get_joke()
print("Here is the wonderful joke for you: ")
print(joke)
engine = pyttsx3.init()
engine.say(joke)
engine.runAndWait()
