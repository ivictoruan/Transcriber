import pyttsx3
import speech_recognition as sr


#inicializando a engine do pyttsx3:
engine = pyttsx3.init()

#configuraçã ode voz
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#parte de ouvir e reconhecer
def ouvir_microfone():
    microfone = sr.Recognizer()
    
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        engine.say("Olá! Meu nome é Jambo! Bota o teu. Fala aí")
        print('fala ai')
        engine.runAndWait()
        engine.stop()
        audio = microfone.listen(source)
    try: 
        frase = microfone.recognize_google(audio, language = 'pt-BR')
        print(frase)
        engine.setProperty('rate', 183)
        engine.say("Você disse: " + frase)
        engine.runAndWait()
        engine.stop()
        engine.say("Eu não entendo mas pelo menos agora eu falo e escuto" )
        engine.runAndWait()
        engine.stop()
    except sr.UnknownValueError:
        print('Não entendi')
    
    return frase



           
ouvir_microfone()


#parte falada
#engine.say("Olá! Meu nome é Jambo! Eu não sei escutar e não entendo ainda mas pelo menos já sei falar ")
engine.runAndWait()
engine.stop()

