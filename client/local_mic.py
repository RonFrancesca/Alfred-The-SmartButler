class Mic:
    prev = None

    def __init__(self, lmd, dictd, lmd_persona, dictd_persona):
        return

    def passiveListen(self, PERSONA):
        return True, "ALFRED"

    def activeListen(self, THRESHOLD=None, LISTEN=True, MUSIC=False):
        if not LISTEN:
            return self.prev

        input = raw_input("YOU: ")
        self.prev = input
        return input

    def say(self, phrase, OPTIONS=None):
        print "ALFRED: " + phrase
