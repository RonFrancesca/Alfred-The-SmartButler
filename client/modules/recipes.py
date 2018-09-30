import re
import urllib2
import json
import rest
import string
import re

WORDS = ["RECIPES","RECIPE"]


def handle(text, mic, profile):
    
    print "I'm recipes.py"
    apiKey='dvxSvo0rQ069QnGwoB7m67Y572Xl4sm3'
    mic.say("What do you want to cook?")
    nome=mic.activeListen()
    mic.say(nome)
    url="http://api.bigoven.com/recipes?pg=1&rpp=25&title_kw=" + nome + "&api_key="+apiKey
    
    data = rest.send('GET', url, headers= {'Accept':'application/json'})
    
    
    
    for item in data['Results']:
        codice = item['RecipeID']
        
    
        print codice
        apiKey='dvxSvo0rQ069QnGwoB7m67Y572Xl4sm3'
        
        url="http://api.bigoven.com/recipe/" + str(codice) + "?api_key="+apiKey
        data = rest.send('GET', url, headers= {'Accept':'application/json'})
        l=data['Instructions']
        title=data['Title']
        
            
        if ((l.find('http://')) < 0):
    
            mic.say("The recipe for " + title)
            Ingredienti= data['Ingredients']
            
            frase = "You will need these ingredients:"
            mic.say(frase)   
            for item in Ingredienti:
                ingrediente = " "
                nome=item['Name']
                quantita=item['DisplayQuantity'] 
                print quantita
                if (quantita==None):
                    quantita = " "
                
                metric=item['MetricUnit']
                ingrediente += quantita
                ingrediente += metric
                ingrediente += nome
                print nome
                
                mic.say(ingrediente)
               
            mic.say("Now we can start the preparation.")
            l=l.replace("w/", " ")
            for line in l.split('\n'):
                print line
                mic.say(line)
            break  
    return
    
def isValid(text):

    return bool(re.search(r'\brecipes|recipe\b', text, re.IGNORECASE))





