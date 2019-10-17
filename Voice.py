from gtts import gTTS
import os
import speech_recognition as sr
import datetime
#from google
#from textblob import TextBlob
import requests
from bs4 import BeautifulSoup
import wolframalpha
import wikipedia
import urllib3
import detector
client = wolframalpha.Client('9YJ2TU-G3W7HK579G')
#-----------------------------------------------------------------------------------------------
#class Analysis:
#    def __init__(self,term):
#        self.term = term
#        self.subjectivity = 0
#        self.sentiment = 0
#        self.url = 'http://www.google.com/search?q={0}'.format(self.term)
#        print(self.url)
#    def run(self):
#        response = requests.get(self.url)
#        # print(response.text)
#        soup = BeautifulSoup(response.text,'html.parser')
       
#        result = soup.find_all('div', attrs={'class':"mraOPb"})
#        if result ==[]:
#            result = soup.find_all('div',attrs={'class':"KpMaL"})
#        for h in result:
#            textTospeech(h.text)cd
#---------------------------------------------------------------------------------------------------

def getfrmggl(command):
    http = urllib3.PoolManager()
    url = 'http://www.google.com/search?q={0}'.format(command)
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    result = soup.find_all('div', attrs={'class':"mraOPb"})
    if result ==[]:
        result = soup.find_all('div',attrs={'class':"KpMaL"})
    for h in result:
        textTospeech(h.text)

def speechTotext():#mycomand
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say any thing..")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='en')
        print(text)
        return  text
    except sr.UnknownValueError:
        assistent(speechTotext())
    except:
        assistent(speechTotext())
    
        
def textTospeech(mytext):#talktome
    print(mytext)
    tts = gTTS(text=mytext, lang='en', slow=False)
    tts.save("welcome.mp3")
    os.system("mpg123 welcome.mp3")

def assistent(command):
    try:
        if command.lower().__contains__('bye'):
            textTospeech("Bye sir, I am loging out , Have a nice day")
            textTospeech("You can call me any time sir")
            mainFun()
        elif command.lower().__contains__('date'):
            now = datetime.datetime.now()
            print (now.strftime("%d-%m-%y"))
            textTospeech(now.strftime("%d-%m-%Y"))
        elif command.lower().__contains__('time'):
            curtime = datetime.datetime.now()
            textTospeech(str(curtime))
        elif command.lower().__contains__('how are you') or command.lower().__contains__('are you fine'):
            textTospeech('I am fine sire')
        elif command.lower().__contains__('hai') or command.lower().__contains__('hello'):
            textTospeech('Hai sir, May i help you')     
        elif command.lower().__contains__('your name') or command.lower().__contains__('who are you'):
            textTospeech('Hai sir, I am Friday. Your personel assistent. What can i do for you...')
        elif command.lower().__contains__('friday') or command.lower().__contains__('fryday'):
            textTospeech('Hai sir, I am Friday. Your personel assistent. What can i do for you...')
        
        else : 
         
            try:
                try:
                    res = client.query(command)
                    results = next(res.results).text
                    textTospeech(results)
                #textTospeech('Do you want to know more')
                    #while True:
                    #    if speechTotext().lower().__contains__('yes'):
                    #        try:
                    #            results = wikipedia.summary(command, sentences=2)
                    #            textTospeech(results)
                    #            break
                    #        except:
                    #            results = wikipedia.summary(command, sentences=2)
                    #            textTospeech(results)
                    #            textTospeech('sorry sir, I only konw this much')
                    #           break
                    #    elif speechTotext().lower().__contains__('no'):
                    #        textTospeech('sorry sir, I only konw this much')
                    #        breakhow to 
                    
                except:
                    results = wikipedia.summary(command, sentences=2)
                    textTospeech(results)
            except:
                getfrmggl(command)
    except:
        
        textTospeech('Sorry')



def callinfun():
    try:
        while True:
            command = speechTotext()
            assistent(command)
    except:
        callinfun()        


def mainFun():
    text = speechTotext()
    text = text.lower()
    while True:
        if text.__contains__('friday') or text.__contains__('fryday'):
            textTospeech("I want to see you  sir")
            stat = detector.faceReg()
            print (stat)
            if(stat == True):
                textTospeech('Hai sir, I am Friday. Your personel assistent. What can i do for you...')
                callinfun()
            else:

                textTospeech("Sorry sir, I did't recognize you")
    



mainFun()

#------------------------------------------
