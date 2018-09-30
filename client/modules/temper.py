from dog import DogGateway
import time
import re
import convertsi
from modules import app_utils

WORDS = ["CHANGE", "TEMPERATURE"]
#if __name__ == '__main__':



def handleResponse(text, mic, profile, temp):
    
    if (app_utils.isNegative(text)):
        mic.say("What temperature do you want me to set?")
        valore=mic.activeListen()
        valore=convertsi.convert(valore)
        mic.say("The temperature has been modified according to your request")
        return str(valore)
        
    if (app_utils.isPositive(text)):
        mic.say("Perfect!")
        return str(temp)
        
    
   
def handle(text, mic, profile):
    
    print " I'm  temper.py"
    dog_zwave = DogGateway('http://dog.polito.it:8088/api/v1/')
    status = dog_zwave.getStatus('TemperatureAndHumiditySensor_76')
    temp = float(status['status']['TemperatureState'][0]['value'][:-1])  
    print '%f degree' % temp
    message="The temperature is %f degrees, is it ok?" % temp
    mic.say(message)
    prova = handleResponse(mic.activeListen(), mic, profile, temp)
    return prova
        
    
def isValid(text):

    return bool(re.search(r'\bchange|temperature\b', text, re.IGNORECASE))
