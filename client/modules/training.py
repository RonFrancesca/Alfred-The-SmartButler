import re
import temper
import StatusBusy
import StatusOnline
from conversation import Conversation
from modules import app_utils

TEMP_FILENAME = "database"

WORDS = ["TRAINING","SPORT"]


def elaboration():
    n=0
    tot=0
    fp=open(TEMP_FILENAME, "r")
    lines = fp.readlines()
    fp.close()
    valori = []
    for line in lines:
        print line
        valori = line.split()
        tot+=float(valori[0])
        msc = valori[1]
        n+=1
        
    if n==0:
        i=-1
        valori.append(i)
        valori.append(" ")
        print valori
        return valori
    else :
        avg = tot/n
        valori[0]= avg
        valori[1]= msc
        print valori
        return valori


def handle(text, mic, profile):
    
    mic.say("Ok I'm setting training mode")
    values = []
    file=open(TEMP_FILENAME,"a+") 
    
    """StatusBusy.handle(text, mic, profile)"""
    values = elaboration()
    if int(values[0]) == -1:
        temp=temper.handle(text, mic, profile)
        tempe=(str(temp)+" ")
        file.write(tempe)

        
        print temp
        file.flush()
        mic.say("Do you want me to play some music?")
    
        resp = mic.activeListen()
        if (app_utils.isPositive(resp)):
            file.write("YES\n")
            file.flush()
            conversation = Conversation("ALFRED", mic, profile)
            conversation.delegateInput("MUSIC")
        elif (app_utils.isNegative(resp)):
            file.write("NO\n")
            file.flush()
    else :
        string = "the temperature has been set at %s degree according to your past requests." %values[0]
        mic.say(string)
        if values[1]=="YES":
            conversation.delegateInput("MUSIC")
            
            
    
    file.close()
    mic.say("Do you want to set your status on-line?")
    c=mic.activeListen()
    if (app_utils.isPositive(c)):
        """StatusOnline.handle(text, mic, profile)"""
        mic.say("Done")
    if (app_utils.isNegative(c)):
        mic.say("Ok")
    
    
        
        
    



def isValid(text):

    return bool(re.search(r'\btraining|sport\b', text, re.IGNORECASE))
