import Queue
import string
from modules import Gmail
from apscheduler.scheduler import Scheduler
import logging
logging.basicConfig()


class Notifier(object):

    class NotificationClient(object):

        def __init__(self, gather, timestamp):
            self.gather = gather
            self.timestamp = timestamp

        def run(self):
            self.timestamp = self.gather(self.timestamp)

    def __init__(self, profile):
        self.q = Queue.Queue()
        self.profile = profile
        self.notifiers = [
            self.NotificationClient(self.handleEmailNotifications, None),
        ]

        sched = Scheduler()
        sched.start()
        sched.add_interval_job(self.gather, seconds=30)

    def gather(self):
        [client.run() for client in self.notifiers]

    def handleEmailNotifications(self, lastDate):
        
        emails = Gmail.fetchUnreadEmails(self.profile, since=lastDate, markRead=True)
        if emails:
            lastDate = Gmail.getMostRecentDate(emails)

        def styleEmail(e):
            nome = Gmail.getSender(e)
            if string.find(nome,"Google Calendar") != -1:
                return e.get('Subject',' ')
            else:
                return "New email from %s." % Gmail.getSender(e)

        for e in emails:
            self.q.put(styleEmail(e))

        return lastDate

    def getNotification(self):

        try:
            notif = self.q.get(block=False)
            return notif
        except Queue.Empty:
            return None

    def getAllNotifications(self):

        notifs = []

        notif = self.getNotification()
        while notif:
            notifs.append(notif)
            notif = self.getNotification()

        return notifs
