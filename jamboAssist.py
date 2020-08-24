import speech_recognition as sr

#parte de ouvir e reconhecer
def ouvir_microfone():
    microfone = sr.Recognizer()
    
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Pode falar... ")
        audio = microfone.listen(source)
    try: 
        frase = microfone.recognize_google(audio, language = 'pt-BR')
        print("Foi dito:" + frase)
    except sr.UnknownValueError:
        ouvir_microfone()
    
    return frase

#inicialização da função:
ouvir_microfone()

