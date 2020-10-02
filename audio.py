
import speech_recognition as sr

def reconheceVoz():
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic, duration=3)
        print("Diga Sim em 10 Segundos ou se arrependa?")
        microfone = rec.listen(mic, timeout=5) 
        try :
            resposta = rec.recognize_google(microfone, language="pt-br")
            print(resposta)
            if resposta == "sim":
                print("Parabéns Sabia Escolha")
            else:
                print("Beleza Então, Aguarde")
        except :
            print("Não entendi")
reconheceVoz()