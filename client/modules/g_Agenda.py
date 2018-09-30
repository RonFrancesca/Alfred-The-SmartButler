import imaplib
import email
import re
import datetime
import string



WORDS = ["AGENDA", "CALENDAR"]


def extract_body(payload):
    if isinstance(payload,str):
        return payload
    else:
        return '\n'.join([extract_body(part.get_payload()) for part in payload])


def fetchAgendaEmails(profile, since=None, markRead=False, limit=None):

    print "I'm g_Agenda.py"
    conn = imaplib.IMAP4_SSL('imap.gmail.com')
    conn.debug = 0
    conn.login("amiproject.smartup@gmail.com", "1234432112344321")
    conn.select('INBOX', readonly=True)
    
    date = datetime.date.today()
    date = date.strftime("%d-%b-%Y")
    
    msgs = []
    """ SOL2 """        
    result, data = conn.uid('search', None, '(FROM "Google Calendar")','(SENTON {0})'.format(date))
    # search and return uids instead
    i = len(data[0].split()) # data[0] is a space separate string
    if i<=0:
        msgs.append("I am sorry I can't see your agenda right now.")
        
    try:
        
        for x in range(i):
            latest_email_uid = data[0].split()[x] # unique ids wrt label selected
            result, data = conn.uid('fetch', latest_email_uid, '(RFC822)')
            # fetch the email body (RFC822) for the given ID
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            # converts byte literal to string removing b''
            msg = email.message_from_string(raw_email_string)
            date= msg["Date"]
            print date  
            dateobj = datetime.datetime.strptime(date, "%a, %d %b %Y %H:%M:%S +0000")
            timeobj = dateobj.time()
            print timeobj            
            mornStart = datetime.time(2, 45, 1)
            mornEnd = datetime.time(5, 30, 0)
            if mornStart <= timeobj <= mornEnd :
                for part in msg.walk():
                    if part.get_content_type() == "text/plain": # ignore attachments/html
                        body = part.get_payload(decode=True)
                        lista = []
                        lista2 = []
                        lista = string.split(body, 'View your calendar')
                        lista2 = lista[0].split('amiproject.smartup@gmail.com')
                        for elm in lista2:
                            msgs.append(elm)
            else :
                msgs.append("I am sorry I can't see your agenda right now.")
    
    except AttributeError :
        pass
    
    conn.close()
    conn.logout()

    return msgs




def handle(text, mic, profile):

    try:
        msgs = fetchAgendaEmails(profile, limit=1)
        messages = ''.join(msgs)
        print messages
        mic.say(messages)
    except imaplib.IMAP4.error:
        mic.say(
            "I'm sorry. I'm not authenticated to work with your Gmail.")
        return


def isValid(text):

    return bool(re.search(r'\b(calendar|agenda)\b', text, re.IGNORECASE))


