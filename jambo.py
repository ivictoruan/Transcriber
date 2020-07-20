import pyttsx3 

engine = pyttsx3.init()

#configurando a voz
rate = engine.getProperty('rate')
engine.setProperty('rate', 300)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#parte falada
engine.say("Meu nome é Alice Ribeiro Diniz ")
engine.runAndWait()
engine.stop()

engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()




