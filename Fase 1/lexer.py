import tokensAndCons
import re
class Lexer:
    def __init__(self,Text):
        self.Text = Text
    
    def EvaluateLines(self):
        TokensFounded=[]
        LineN=1
        for Element in self.Text:
            PosS=0
            PosE=0
            StringAux = ''
            while PosE < len(Element):
                if Element[PosE] not in ' \n\t':
                    StringAux += Element[PosE]
                    if(re.search(tokensAndCons.Reservadas,StringAux)):
                        StringAux += " línea " + str(LineN) + " col " + str(PosS+1) + '-' + str(PosE+2) + ' es T_' + StringAux
                        PosS = PosE+1
                        TokensFounded.append(StringAux)
                        StringAux =""
                PosE+=1
            LineN += 1
        return TokensFounded

