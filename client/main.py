import yaml
import os
import sys
from conversation import Conversation

TEMP_FILENAME = "database"
file_path = os.path.abspath('./modules')
sys.path.append(file_path)

def isLocal():
    return len(sys.argv) > 1 and sys.argv[1] == "--local"

if isLocal():
    from local_mic import Mic
else:
    from mic import Mic

if __name__ == "__main__":

    print "==========================================================="
    print "                ALFRED the Smart Butler                    "
    print "                  2014 SmartUp! Group                      "
    print "       Copyright 2013 Shubhro Saha & Charlie Marsh         "
    print "==========================================================="

    profile = yaml.safe_load(open("profile.yml", "r"))

    file=open(TEMP_FILENAME,"r+") 

    mic = Mic("languagemodel.lm", "dictionary.dic",
              "languagemodel_persona.lm", "dictionary_persona.dic")

    mic.say("How can I be of service?")

    conversation = Conversation("ALFRED", mic, profile)

    conversation.handleForever()
