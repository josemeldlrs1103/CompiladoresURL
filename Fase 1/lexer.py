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
                    elif (StringAux == '+'):
                        StringAux += " línea " + str(LineN) + " col " + str(PosS+1) + '-' + str(PosE+2) + ' es ' + tokensAndCons.TKN_PLUS
                        PosS = PosE+1
                        TokensFounded.append(StringAux)
                        StringAux =""
                    elif (StringAux == '-'):
                        StringAux += " línea " + str(LineN) + " col " + str(PosS+1) + '-' + str(PosE+2) + ' es ' + tokensAndCons.TKN_MINUS
                        PosS = PosE+1
                        TokensFounded.append(StringAux)
                        StringAux =""
                    elif (StringAux == '*'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '*/'):
                                StringAux2 += " línea " + str(LineN) + " col " + str(PosS+1) + '-' + str(PosE+2) + ' es ' + tokensAndCons.TKN_CMT_CLOSE
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(StringAux2)
                                StringAux2 =""
                                StringAux =""
                            else:
                                StringAux += " línea " + str(LineN) + " col " + str(PosS+1) + '-' + str(PosE+2) + ' es ' + tokensAndCons.TKN_MULT
                                PosS = PosE+1
                                TokensFounded.append(StringAux)
                                StringAux =""
                        except:
                            StringAux += " línea " + str(LineN) + " col " + str(PosS+1) + '-' + str(PosE+2) + ' es ' + tokensAndCons.TKN_MULT
                            PosS = PosE+1
                            TokensFounded.append(StringAux)
                            StringAux =""
                    elif (StringAux == '/'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '//'):
                                StringAux2 += " línea " + str(LineN) + " col " + str(PosS+1) + '-' + str(PosE+2) + ' es ' + tokensAndCons.TKN_CMT_LINE
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(StringAux2)
                                StringAux2 =""
                                StringAux =""
                            elif (StringAux2 == '/*'):
                                StringAux2 += " línea " + str(LineN) + " col " + str(PosS+1) + '-' + str(PosE+2) + ' es ' + tokensAndCons.TKN_CMT_OPEN
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(StringAux2)
                                StringAux2 =""
                                StringAux =""
                            else:
                                 StringAux += " línea " + str(LineN) + " col " + str(PosS+1) + '-' + str(PosE+2) + ' es ' + tokensAndCons.TKN_DIV
                                PosS = PosE+1
                                TokensFounded.append(StringAux)
                                StringAux =""
                        except:
                            StringAux += " línea " + str(LineN) + " col " + str(PosS+1) + '-' + str(PosE+2) + ' es ' + tokensAndCons.TKN_DIV
                            PosS = PosE+1
                            TokensFounded.append(StringAux)
                            StringAux =""
                PosE+=1
            LineN += 1
        return TokensFounded

