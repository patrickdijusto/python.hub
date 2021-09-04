import pyttsx3

engine = pyttsx3.init()

engine.say("This is the voice of world control.  I bring you peace.  it may be the peace of plenty and content.  or the peace of unburied death.  The choice is yours.  Obey me and live, or disobey and die.")

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #changing index changes voices but ony 0 and 1 are working here
engine.say('Hello World')


index = 0
for voice in voices:
   print(f'index-> {index} -- {voice.name}')
   index +=1

   print(voice)

engine.say('Hello World')


engine.runAndWait()

