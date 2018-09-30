class Mic:

    def __init__(self, inputs):
        self.inputs = inputs
        self.idx = 0
        self.outputs = []

    def passiveListen(self, PERSONA):
        return True, "JASPER"

    def activeListen(self, THRESHOLD=None, LISTEN=True, MUSIC=False):
        if not LISTEN:
            return self.inputs[self.idx - 1]

        input = self.inputs[self.idx]
        self.idx += 1
        return input

    def say(self, phrase, OPTIONS=None):
        self.outputs.append(phrase)
