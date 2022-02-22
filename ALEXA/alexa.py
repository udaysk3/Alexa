import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import smtplib

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate", 175)


def speakcommand(command):
        engine.say(command)
        engine.runAndWait()

def wish():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            return 'good morning'
        elif hour>=12 and hour<=18:
            return 'good afternoon'
        else:
            return 'good evening'

def sendmail():
      speakcommand('enter sender mail : ')
      sender_mail = input('enter sender mail : ')
      speakcommand('enter sender mail password : ')
      sender_password = input('enter sender mail password : ')
      speakcommand('enter receiver mail : ')
      receiver_mail = input('enter receiver mail : ')
      

      speakcommand('enter the message ')
      message = input('enter your message : ')
      try:
        server = smtplib.SMTP(host='smtp.gmail.com')
        server.starttls()
            
        server.login(user = sender_mail,password=sender_password)
        server.sendmail(from_addr=sender_mail,to_addrs=receiver_mail,msg=message)
        print('Mail sent successfully !')
      except:
          print('Error while sending Email. Please try again')
          speakcommand('Error while sending Email  Please try again')
          print('please check if you have allowed low secure apps')
          speakcommand('please check if you have allowed low secured apps in your\
           sender google accout')

def run():
    def takecommand():
        try:
            with sr.Microphone() as source:
                print('listening')
                listener.pause_threshold = 1
                audio = listener.listen(source)
                command = listener.recognize_google(audio)
                command = command.lower()
                print(command)
                speakcommand(command)
                return command
        except:
            pass
        
    



    def analyzecommand():
        command = takecommand()
        if 'hello' in command:
            print('hi '+ wish())
            speakcommand('hi '+wish())
        elif 'open' in command:
            command = command.replace('open ','')
            print('opening...')
            speakcommand('opening')
            webbrowser.open('https://www.'+command+'.com')
        elif 'play' in command:
            command = command.replace('play','')
            pywhatkit.playonyt(command)
        elif 'who is' in command:
            person = command.replace('who is ', '')
            print('Searching for '+person)
            speakcommand('Searching for '+person)
            try:
                info = wikipedia.summary(person,2,auto_suggest=False)
                print(info)
                speakcommand(info)
            except:
                print('please try another command')
                speakcommand('please try another command')
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            speakcommand(joke)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speakcommand(time)
        elif 'say hi' in command:
            command = command.replace('say hi to','')
            print('hi',command)
            speakcommand('hi'+command)
        elif 'mail' in command:
            sendmail()
        elif 'bye' in command:
            print('Have a Great day!')
            speakcommand('Have a Great day!')
            exit()
        else:
            print('please repeat again! or that is not implemented yet')
            speakcommand('please repeat again or that is not implemented yet')
        
    try:
        analyzecommand()
    except:
        pass

engine.say('hello uday sir'+wish()+' I am your alexa  how may i help you ')
engine.runAndWait()
while True:
    run()


