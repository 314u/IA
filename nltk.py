
import speech_recognition as sr
import nltk
from gtts import gTTS
from playsound import playsound
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")
        
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:
        
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')
        
        #Retorna a frase pronunciada
        print("Você disse: " + frase)
        
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
        
    return frase

#Funcao responsavel por falar 
def cria_audio(audio):
    tts = gTTS(audio,lang='pt-br')
    #Salva o arquivo de audio
    tts.save('hello.mp3')
    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    playsound('hello.mp3')

def printAudioOnFile(audio,nome):
    arquivo = open(nome,'w')
    arquivo.write(audio)
    arquivo.close()


def verifyWord():
    arquivo = open('audioTranscrito.txt','r')
    texto = arquivo.readline()
    words =  nltk.tokenize.word_tokenize(texto)

    words.concordance("sim")
   
def verifySentences():
    audio1 = ouvir_microfone()
    audio2 = ouvir_microfone()

    printAudioOnFile(audio1,"audio1.txt")
    printAudioOnFile(audio2,"audio2.txt")
    
    arquivo1 = open('audio1.txt','r')
    arquivo2 = open('audio2.txt','r')

    texto1 = arquivo1.readline()
    texto2 = arquivo2.readline()

    semelhanca = fuzz.ratio(texto1,texto2)

    if semelhanca>70:
        print("Os textos sao iguais")