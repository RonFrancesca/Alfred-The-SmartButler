def convert(temp):
    WORDS= ['SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN','TWENTY','TWENTYONE','TWENTYTWO','TWENTYTHREE','TWENTYFOUR','TWENTYFIVE','TWENTYSIX']
    VALUES=[16,17,18,19,20,21,22,23,24,25,26]
    
    for i in range(0,11):
        if temp==WORDS[i]:
            print VALUES[i]
            return VALUES[i]
