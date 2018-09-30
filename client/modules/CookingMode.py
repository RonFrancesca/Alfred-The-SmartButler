import Threadh
import re
import recipes
import rest
import temper
import StatusBusy
import StatusOnline
import Alarm
from modules import app_utils




WORDS = ["COOKING", "COOKINGMODE"]




def handle(text, mic, profile):
    print "I'm Cooking_mode.py"
    mic.say("OK. I'm setting cooking_mode")
    StatusBusy.handle(text, mic, profile)
    temper.handle(text, mic, profile)
    recipes.handle(text, mic, profile)
    mic.say("Do you want to set an alarm?")
    response=mic.activeListen()
    if (app_utils.isPositive(response)):
        ret=alarm.handle(text, mic, profile)    
            
    statuson(text, mic, profile)
                
    return  

def statuson(text, mic, profile):
    mic.say("Do you want to set your status on-line?")
    c=mic.activeListen()
    if (app_utils.isPositive(c)):
        StatusOnline.handle(text, mic, profile)
        mic.say("Done")
    if (app_utils.isNegative(c)):
        mic.say("Ok")
    return
    
            
def isValid(text):
    
    return bool(re.search(r'\bcooking_mode|cooking\b', text, re.IGNORECASE))
  
   



    
