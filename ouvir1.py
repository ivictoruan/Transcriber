import speech_recognition as sr

def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio, key="AIzaSyDRdSN1VaRW27HxA68rZW5FesS2qoPD8", language='pt-BR', show_all=True)
        print("Você disse: " + frase)
    except sr.UnKownValueError:
        print("Não entendi")
        return frase
ouvir_microfone()
