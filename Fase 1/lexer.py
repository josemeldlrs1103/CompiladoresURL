import tokensAndCons
import re
class Lexer:
    def __init__(self,Text):
        self.Text = Text
    
    def fillAux (self, token, line, colStart, colEnd, tokenID):
        result = token + ' línea ' + str(line) + ' col ' + str(colStart) + '-' +str(colEnd) + ' es: ' + tokenID
        return result
    
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
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,'T_'+StringAux))
                        StringAux = ''
                    elif (StringAux == '+'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_PLUS))
                        StringAux = ''
                    elif (StringAux == '-'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MINUS))
                        StringAux = ''
                    elif (StringAux == '*'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '*/'):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_CMT_CLOSE))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MULT))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MULT))
                            StringAux = ''
                    elif (StringAux == '/'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '//'):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_CMT_LINE))
                                StringAux2 = ''
                                StringAux = ''
                            elif (StringAux2 == '/*'):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_CMT_OPEN))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_DIV))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_DIV))
                            StringAux = ''
                    elif (StringAux == '%'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_PRCTGE))
                        StringAux = ''
                    elif (StringAux == '<'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '<='):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MINEQLS))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MINOR))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MINOR))
                            StringAux = ''
                    elif (StringAux == '>'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '>='):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MAJEQLS))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MAJOR))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MAJOR))
                            StringAux = ''
                    elif (StringAux == '='):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '=='):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_DBLEQLS))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_EQUALS))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_EQUALS))
                            StringAux = ''
                    elif (StringAux == '!'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '!='):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_DISTINCT))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_EXCMARK))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_EXCMARK))
                            StringAux = ''
                    elif (StringAux == '&'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '&&'):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_AND))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                #definir error, operador debe ser binario
                                PosS = PosE+1
                                StringAux = ''
                        except:
                            #definir error, operador debe ser binario
                            PosS = PosE+1
                            StringAux = ''
                    elif (StringAux == '|'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '||'):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_AND))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                #definir error, operador debe ser binario
                                PosS = PosE+1
                                StringAux = ''
                        except:
                            #definir error, operador debe ser binario
                            PosS = PosE+1
                            StringAux = ''
                    elif (StringAux == ';'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_SEMICOLON))
                        StringAux = ''
                    elif (StringAux == ','):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_COMMA))
                        StringAux = ''
                    elif (StringAux == '.'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_DOT))
                        StringAux = ''
                    elif (StringAux == '('):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '()'):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_PAREN))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_PAREN_L))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_PAREN_L))
                            StringAux = ''
                    elif (StringAux == ')'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_PAREN_R))
                        StringAux = ''
                    elif (StringAux == '['):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '[]'):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_SQRBRKT))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_SQRBRKT_L))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_SQRBRKT_L))
                            StringAux = ''
                    elif (StringAux == ']'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_SQRBRKT_R))
                        StringAux = ''
                    elif (StringAux == '{'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '{}'):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_BRKT))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_BRKT_L))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_BRKT_L))
                            StringAux = ''
                    elif (StringAux == '}'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_BRKT_R))
                        StringAux = ''
                PosE+=1
            LineN += 1
        return TokensFounded

