import Threadh
import re



WORDS = ["ALARM"]


def handle(text, mic, profile):
   
    print "I'm Alarm.py"
    mic.say("How many minutes I have to wait from now?")
    minuti=mic.activeListen()
    string = "I will alert you in %s minutes" % minuti
    mic.say(string)
    a = Threadh.mythread()
    l=a.start(minuti*60)
    mic.say("The countdown is finished")
    return l
    

    



def isValid(text):
    
    return bool(re.search(r'\balarm\b', text, re.IGNORECASE))
