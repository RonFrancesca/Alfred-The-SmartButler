import threading
import time

class mythread():
    
    def run(self,secondi):
        time.sleep(secondi)
        return 1
    
    def start(self,secondi):
        return(self.run(secondi))
        
