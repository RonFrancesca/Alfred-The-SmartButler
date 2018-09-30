import urllib
import re
from facepy import GraphAPI



WORDS = ["BUSY"]

def handle(text, mic, profile):
    
    print "I'm Busy.py"
    token = "CAACEdEose0cBAOs8kQn5iLHkd3ZCObZCEZC7IAfXZBt8ZCFyx9ESVP6N3JNDki9cQZApw2GLg6m2vNjhIiK9hjwtt88bs5O58D1cZBPTo5RnFafSOvOODQsLhnXN8jjezYTfZA1b2qARsH9AR9zmuEaTRaauktr1Tj4rhDZARMPI1ViAh3GK6iWcbwhWCZCuFRkI7v7TR5TiSEgPmCKbnUKXXe"
    graph = GraphAPI(token)
    postid = graph.post(path = 'me/feed',message = "I'm busy")
    print postid
    mic.say("Busy mode on")
    


def isValid(text):
    
    return bool(re.search(r'\bbusy\b', text, re.IGNORECASE))
