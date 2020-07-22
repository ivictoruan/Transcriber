import speech_recognition as sr


rec = sr.Recognizer()

mic = sr.Microphone()

with mic as sourcer:
    rec.adjust_for_ambient_noise(source)
    print("Olá...")
    audio = rec.listen(fonte)
    print("Reconhecendo...")
    try:
         #Passa a variável para o algoritmo reconhecedor de padroes
        text = rec.recognize_google(audio, language = "pt-BR")
        print("Você disse: {}".format(text))
    except sr.UnknownValueError:
        print("Não entendi")
        
    return text