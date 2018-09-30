import feedparser
import app_utils
import re
from semantic.numbers import NumberService

WORDS = ["NEWS", "YES", "NO"]

PRIORITY = 3

URL = 'http://news.ycombinator.com'


class Article:

    def __init__(self, title, URL):
        self.title = title
        self.URL = URL


def getTopArticles(maxResults=None):
    d = feedparser.parse("http://news.google.com/?output=rss")

    count = 0
    articles = []
    for item in d['items']:
        articles.append(Article(item['title'], item['link'].split("&url=")[1]))
        count += 1
        if maxResults and count > maxResults:
            break

    return articles


def handle(text, mic, profile):

    print "I'm News.py"
    
    mic.say("Pulling up the news")
    articles = getTopArticles(maxResults=3)
    titles = [" ".join(x.title.split(" - ")[:-1]) for x in articles]
    all_titles = "... ".join(str(idx + 1) + ")" +
                             title for idx, title in enumerate(titles))
    mic.say("Here are the current top headlines. " + all_titles)

    

     


def isValid(text):
    
    return bool(re.search(r'\b(news|headline)\b', text, re.IGNORECASE))
