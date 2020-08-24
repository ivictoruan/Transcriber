import speech_recognition as sr

# parte de ouvir e reconhecer
def ouvir_microfone():
    on = True
    while on:
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            #ajuste para ruidos no ambiente
            microfone.adjust_for_ambient_noise(source)
            print('"Terminar aula" para SAIR')
            audio = microfone.listen(source)
            try:
                frase = microfone.recognize_google(audio, language="pt-BR")
                print("Foi dito:    " + frase)
                if frase == 'terminar aula':
                    break
            except sr.UnknownValueError:
                ouvir_microfone()
            #return frase
    else:
        ouvir_microfone()



# inicialização da função:
ouvir_microfone()

