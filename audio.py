
import speech_recognition as sr
import nltk
from gtts import gTTS
from playsound import playsound

#Funcao responsavel por falar 
def cria_audio(audio):
    tts = gTTS(audio,lang='pt-br')
    #Salva o arquivo de audio
    tts.save('hello.mp3')
    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    playsound('hello.mp3')

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