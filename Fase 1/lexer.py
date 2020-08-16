import tokensAndCons

class Lexer:
     def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        for element in text:
            printElement (element)
            
def printElement(element):
        print (element)
   