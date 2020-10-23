import tokensAndCons
import re
import errorManager
import stateNode
ErrorQuantity = 0
class Lexer:

    def __init__(self,Text):
        self.Text = Text
    
    def fillAux (self, token, line, colStart, colEnd, tokenID):
        result = token + ' línea ' + str(line) + ' col ' + str(colStart) + '-' +str(colEnd) + ' es: ' + tokenID
        return result

    def ParserList(self, tokenID):
        result = tokenID
        return result
    
    def countError(self):
        global ErrorQuantity
        ErrorQuantity += 1
    


    def EvaluateLines(self):
        TokensFounded=[]
        IdTokens = []
        LineN=1
        StringStart = 0
        CommentStart = 0
        OpenString = None
        OpenComment = None
        AuxFlag = False
        for Element in self.Text:
            PosS=0
            PosE=0
            if(AuxFlag==False):
                StringAnalizer=''
                LastRecognition=''
            Prior = None
            DecimalExist= False
            AnalizedChar =True
            DiscardChars = False
            while PosE < len(Element):
                StringAux = ''
                StringAux += Element[PosE]
                StringAnalizer += Element[PosE]
                if(re.search(tokensAndCons.Reservadas1,StringAnalizer)):
                    AnalizedChar = True
                    LastRecognition = 'Reservada'
                    if(StringAnalizer=='int' or StringAnalizer=='for' or StringAnalizer=='New'):
                        indx = PosE
                        if(StringAnalizer=='int' and PosE<=(len(Element)-7)):
                            if(Element[indx+1]=='e' and Element[indx+2]=='r' and Element[indx+3]=='f' and Element[PosE+4]=='a' and Element[PosE+5]=='c' and Element[PosE+6]=='e'):
                                Prior =False
                            else:
                                Prior = True
                        else:
                            Prior = True
                        if(StringAnalizer=='for' and PosE<=(len(Element)-5)):
                            if(Element[PosE+1]=='e' and Element[PosE+2]=='a' and Element[PosE+3]=='c' and Element[PosE+4]=='h'):
                                Prior =False
                            else:
                                Prior = True
                        else:
                            if(Prior != False):
                                Prior = True
                        if(StringAnalizer=='New' and PosE<=(len(Element)-6)):
                            if(Element[PosE+1]=='A' and Element[PosE+2]=='r' and Element[PosE+3]=='r' and Element[PosE+4]=='a' and Element[PosE+5]=='y'):
                                Prior =False
                            else:
                                Prior = True    
                        else:
                            if(Prior != False):
                                Prior = True
                    else:
                        Prior = True
                elif(re.search(tokensAndCons.Identifiers,StringAnalizer)):
                        AnalizedChar =True
                        LastRecognition = 'identifier'
                        if(StringAnalizer == 'true' or StringAnalizer== 'false'):
                            LastRecognition = 'Booleano'
                elif(re.search(tokensAndCons.Enteros, StringAnalizer)):
                    AnalizedChar = True
                    LastRecognition = 'Integer'
                elif(re.search(tokensAndCons.TempHex,StringAnalizer)):
                    AnalizedChar =True
                    LastRecognition = 'Inicio hex'
                elif(re.search(tokensAndCons.Double, StringAnalizer)):
                    AnalizedChar = True
                    LastRecognition = 'Double'
                    DecimalExist =True
                elif(re.search(tokensAndCons.TempDouble, StringAnalizer)):
                    if((PosE < len(Element)-3) and (Element[PosE+1] in '+-1234567890')):
                        if(Element[PosE+1] in '1234567890'):
                            AnalizedChar = True
                        elif(Element[PosE+1] in '+-' and Element[PosE+2] in '1234567890'):
                            AnalizedChar = True
                        else:
                            AnalizedChar =False
                            Prior = True
                    else:
                        AnalizedChar = False
                        Prior = True
                    LastRecognition = 'Inicio dob'
                elif(re.search(tokensAndCons.StringStep1,StringAnalizer)):
                    OpenString = True
                    LastRecognition = 'String'
                    StringStart = LineN
                elif(re.search(tokensAndCons.StringStep2,StringAnalizer)):
                    OpenString = False
                    LastRecognition = 'String'
                elif(re.search(tokensAndCons.OneLineCommentsStep1, StringAnalizer)):
                    if(PosE<= (len(Element)-2)):
                        if(Element[PosE+1]=='/'):
                            LastRecognition = 'Comment Line'
                        if(Element[PosE+1]=='*'):
                            LastRecognition = 'Multi-Line Comment'
                elif(re.search(tokensAndCons.OneLineCommentsStep2,StringAnalizer)):
                    LastRecognition = 'Comment Line'
                elif(re.search(tokensAndCons.MultiLineCommentsStep1, StringAnalizer)):
                    if(LastRecognition != 'Multi-Line Comment'):
                        if(Element[PosE+1]=='/'):
                            LastRecognition = 'Multi-Line Comment'
                    OpenComment =True
                    CommentStart = LineN
                elif(re.search(tokensAndCons.MultiLineCommentsStep2, StringAnalizer)):
                    LastRecognition = 'SCMulti-Line Comment'
                elif(re.search(tokensAndCons.MultiLineCommentsStep3, StringAnalizer)):
                    LastRecognition = 'Multi-Line Comment'
                    OpenComment = False
                    StringAnalizer = ''
                    AuxFlag = False
                elif(re.search(tokensAndCons.ExtraCaseComment,StringAnalizer)):
                    if(PosE <= (len(Element)-2)):
                        StringAnalizer = StringAnalizer[0:2]
                        if(StringAux=='*' and Element[PosE+1]=='/'):
                          StringAnalizer += Element[PosE]
                        if(LastRecognition == 'SCMulti-Line Comment'):
                            StringAnalizer = '/**'
                else:
                    if(len(StringAnalizer)>1 and LastRecognition!=''):
                        if(StringAnalizer!='\n'):
                            StringAnalizer = StringAnalizer[:-1]
                        if( LastRecognition == 'Reservada'):
                            if(Prior == True):
                                if(StringAux in ' \n\t'):
                                    StringAnalizer += Element[PosE]
                                TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_'+StringAnalizer))
                                IdTokens.append(stateNode.LToken('T_'+StringAnalizer,LineN))
                                Prior=False
                                if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                                    AnalizedChar = False
                        elif(LastRecognition == 'identifier'):
                            if(DiscardChars==False):
                                TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_'+LastRecognition))
                                IdTokens.append(stateNode.LToken('T_'+LastRecognition,LineN))
                            if(StringAux!='' and StringAux!=' ' and StringAux!='\t' and StringAux!='\n' and StringAux!='+' and StringAux!='-' and StringAux!='*' and StringAux!='/' and StringAux!='%' and StringAux!='<' and StringAux!='>' and StringAux!='=' and StringAux!='!' and StringAux!='&' and StringAux!='|' and StringAux!=';' and StringAux!=',' and StringAux!='.' and StringAux!='(' and StringAux!=')' and StringAux!='[' and StringAux!=']' and StringAux!='{' and StringAux!='}'):
                                DiscardChars = True
                            else:
                                DiscardChars = False
                                LastRecognition = ''
                        elif(LastRecognition == 'Booleano'):
                            TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,tokensAndCons.TKN_BOOLCONST))
                            IdTokens.append(stateNode.LToken(tokensAndCons.TKN_BOOLCONST,LineN))
                            if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                                 AnalizedChar = False
                        elif(LastRecognition == 'Integer'):
                            TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,tokensAndCons.TKN_INTCONST))
                            IdTokens.append(stateNode.LToken(tokensAndCons.TKN_INTCONST,LineN))
                            if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                                AnalizedChar = False
                        elif(LastRecognition == 'Double'):
                            TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,tokensAndCons.TKN_DOUBCONST))
                            IdTokens.append(stateNode.LToken(tokensAndCons.TKN_DOUBCONST,LineN))
                            if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                                AnalizedChar = False
                        elif(LastRecognition == 'Inicio Hex' or LastRecognition == 'Inicio dob'):
                            TokensFounded.append(errorManager.incomplete(LineN,StringAnalizer))
                            self.countError()
                            if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                                AnalizedChar = False
                    else:
                        if(StringAux not in ' \n\t:+-*/%<>=!&|;,.()[]}{'):
                            TokensFounded.append(errorManager.notValid(LineN,StringAnalizer))
                            self.countError()
                            StringAnalizer=''
                    if (StringAnalizer != '\n'):
                        StringAnalizer=''
                    if(StringAux not in ' \n\t'):
                        PosS = PosE
                    else:
                        PosS = PosE+1               
                if(Prior==True):
                    if(LastRecognition == 'Reservada'):
                        TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_'+StringAnalizer))
                        IdTokens.append(stateNode.LToken('T_'+StringAnalizer,LineN))
                    elif(LastRecognition == 'Inicio dob'):
                        StringAnalizer = StringAnalizer[:-1]
                        TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_Double'))
                        IdTokens.append(stateNode.LToken('T_Double',LineN))
                    Prior=False
                    StringAnalizer=''
                if (StringAux == '\n'):
                    if(StringAnalizer!='\n'):
                        StringAnalizer = StringAnalizer[:-1]
                    if( LastRecognition == 'Reservada'):
                            if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                                TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_'+StringAnalizer))
                                IdTokens.append(stateNode.LToken('T_'+StringAnalizer,LineN))
                                AnalizedChar = False
                    elif(LastRecognition == 'identifier'):
                        if(DiscardChars==False):
                            TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_'+LastRecognition))
                            IdTokens.append(stateNode.LToken('T_'+LastRecognition,LineN))
                            if(StringAux!='' and StringAux!=' ' and StringAux!='\t' and StringAux!='\n' and StringAux!='+' and StringAux!='-' and StringAux!='*' and StringAux!='/' and StringAux!='%' and StringAux!='<' and StringAux!='>' and StringAux!='=' and StringAux!='!' and StringAux!='&' and StringAux!='|' and StringAux!=';' and StringAux!=',' and StringAux!='.' and StringAux!='(' and StringAux!=')' and StringAux!='[' and StringAux!=']' and StringAux!='{' and StringAux!='}'):
                                DiscardChars = True
                            else:
                                DiscardChars = False
                                LastRecognition = ''
                    elif(LastRecognition == 'Booleano'):
                        if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                            TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,tokensAndCons.TKN_BOOLCONST))
                            IdTokens.append(stateNode.LToken(tokensAndCons.TKN_BOOLCONST,LineN))
                            AnalizedChar = False
                    elif(LastRecognition == 'Integer'):
                        if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                            TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,tokensAndCons.TKN_INTCONST))
                            IdTokens.append(stateNode.LToken(tokensAndCons.TKN_INTCONST,LineN))
                            AnalizedChar = False
                    elif(LastRecognition == 'Double'):
                        if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                            TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,tokensAndCons.TKN_DOUBCONST))
                            IdTokens.append(stateNode.LToken(tokensAndCons.TKN_DOUBCONST,LineN))
                            AnalizedChar = False
                    elif(LastRecognition == 'Inicio Hex' or LastRecognition == 'Inicio dob'):
                        TokensFounded.append(errorManager.incomplete(LineN,StringAnalizer))
                        if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                            AnalizedChar = False
                    else:
                        if(StringAux not in ' \n\t+-*/%<>=!&|;,.()[]}{'):
                            TokensFounded.append(errorManager.notValid(LineN,StringAnalizer))
                            self.countError()
                    if (LastRecognition != 'Multi-Line Comment' and StringAnalizer!= '\n'):
                        StringAnalizer=''
                    if(StringAux not in ' \n\t'):
                        PosS = PosE
                    else:
                        PosS = PosE+1
                    if(LastRecognition== 'Comment Line'):
                        StringAnalizer = ''
                if(AnalizedChar == False):
                    StringAux = ''
                if(OpenString == False):
                    Temp = StringAnalizer[1:-1]
                    if('\"' not in Temp and chr(0) not in Temp):
                        TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_String'+StringAnalizer))
                        IdTokens.append(stateNode.LToken(tokensAndCons.TKN_STRCONST,LineN))
                    else:
                        TokensFounded.append('Error encontrado en línea ' + LineN + ', la cadena presente en la línea contiene un caracter no válido')
                        self.countError()
                    StringAnalizer = ''
                    OpenString = None
                    LastRecognition = ''
                if(LastRecognition == 'String' or LastRecognition == 'Comment Line' or LastRecognition == 'Multi-Line Comment' or LastRecognition == 'SCMulti-Line Comment'):
                    StringAux =''
                if (StringAux == '+'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_PLUS))
                        IdTokens.append(stateNode.LToken(tokensAndCons.TKN_PLUS,LineN))
                        StringAux = ''
                elif (StringAux == '-'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MINUS))
                        IdTokens.append(stateNode.LToken(tokensAndCons.TKN_MINUS,LineN))
                        StringAux = ''
                elif (StringAux == '*'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '*/'):
                                PosS = PosE+1
                                PosE+=1
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MULT))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_MULT,LineN))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MULT))
                            IdTokens.append(stateNode.LToken(tokensAndCons.TKN_MULT,LineN))
                            StringAux = ''
                elif (StringAux == '/'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '//'):
                                PosS = PosE+1
                                PosE+=1
                                StringAux2 = ''
                                StringAux = ''
                            elif (StringAux2 == '/*'):
                                PosS = PosE+1
                                PosE+=1
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_DIV))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_DIV,LineN))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_DIV))
                            IdTokens.append(stateNode.LToken(tokensAndCons.TKN_DIV,LineN))
                            StringAux = ''
                elif (StringAux == '%'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_PRCTGE))
                        IdTokens.append(stateNode.LToken(tokensAndCons.TKN_PRCTGE,LineN))
                        StringAux = ''
                elif (StringAux == '<'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '<='):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MINEQLS))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_MINEQLS,LineN))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MINOR))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_MINOR,LineN))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MINOR))
                            IdTokens.append(stateNode.LToken(tokensAndCons.TKN_MINOR,LineN))
                            StringAux = ''
                elif (StringAux == '>'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '>='):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MAJEQLS))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_MAJEQLS,LineN))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MAJOR))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_MAJOR,LineN))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_MAJOR))
                            IdTokens.append(stateNode.LToken(tokensAndCons.TKN_MAJOR,LineN))
                            StringAux = ''
                elif (StringAux == '='):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '=='):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_DBLEQLS))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_DBLEQLS,LineN))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_EQUALS))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_EQUALS,LineN))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_EQUALS))
                            IdTokens.append(stateNode.LToken(tokensAndCons.TKN_EQUALS,LineN))
                            StringAux = ''
                elif (StringAux == '!'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '!='):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_DISTINCT))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_DISTINCT,LineN))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_EXCMARK))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_EXCMARK,LineN))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_EXCMARK))
                            IdTokens.append(stateNode.LToken(tokensAndCons.TKN_EXCMARK,LineN))
                            StringAux = ''
                elif (StringAux == '&'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '&&'):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_AND))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_AND,LineN))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                TokensFounded.append(errorManager.incomplete(LineN,StringAux))
                                self.countError()
                                PosS = PosE+1
                                StringAux = ''
                        except:
                            TokensFounded.append(errorManager.incomplete(LineN,StringAux))
                            self.countError()
                            PosS = PosE+1
                            StringAux = ''
                elif (StringAux == '|'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '||'):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_AND))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_AND,LineN))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                TokensFounded.append(errorManager.incomplete(LineN,StringAux))
                                self.countError()
                                PosS = PosE+1
                                StringAux = ''
                        except:
                            TokensFounded.append(errorManager.incomplete(LineN,StringAux))
                            self.countError()
                            PosS = PosE+1
                            StringAux = ''
                elif (StringAux == ':'):
                    PosS = PosE+1
                    TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_COLON))
                    IdTokens.append(stateNode.LToken(tokensAndCons.TKN_COLON,LineN))
                    StringAux = ''
                elif (StringAux == ';'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_SEMICOLON))
                        IdTokens.append(stateNode.LToken(tokensAndCons.TKN_SEMICOLON,LineN))
                        StringAux = ''
                elif (StringAux == ','):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_COMMA))
                        IdTokens.append(stateNode.LToken(tokensAndCons.TKN_COMMA,LineN))
                        StringAux = ''
                elif (StringAux == '.'):
                    if(DecimalExist== False):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_DOT))
                        IdTokens.append(stateNode.LToken(tokensAndCons.TKN_DOT,LineN))
                        StringAux = ''
                elif (StringAux == '('):
                        if (re.search(tokensAndCons.ERParentesis, Element)):
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_PAREN_L))
                            IdTokens.append(stateNode.LToken(tokensAndCons.TKN_PAREN_L,LineN))
                            StringAux = ''
                        else:
                            PosS = PosE+1
                            TokensFounded.append(errorManager.expected(LineN,PosS+1, '(', ')'))
                            self.countError()
                            StringAux = ''
                elif (StringAux == ')'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_PAREN_R))
                        IdTokens.append(stateNode.LToken(tokensAndCons.TKN_PAREN_R,LineN))
                        StringAux = ''
                elif (StringAux == '['):
                        if (re.search(tokensAndCons.ERCorchetes, Element)):
                            try:
                                StringAux2 = StringAux + Element[PosE+1]
                                if (StringAux2 == '[]'):
                                    PosS = PosE+1
                                    PosE+=1
                                    TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_SQRBRKT))
                                    IdTokens.append(stateNode.LToken(tokensAndCons.TKN_SQRBRKT,LineN))
                                    StringAux2 = ''
                                    StringAux = ''
                                else:
                                    PosS = PosE+1
                                    TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_SQRBRKT_L))
                                    IdTokens.append(stateNode.LToken(tokensAndCons.TKN_SQRBRKT_L,LineN))
                                    StringAux = ''
                            except:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_SQRBRKT_L))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_SQRBRKT_L,LineN))
                                StringAux = ''
                        else:
                            PosS = PosE+1
                            TokensFounded.append(errorManager.expected(LineN,PosS+1, '[', ']'))
                            self.countError()
                            StringAux = ''
                elif (StringAux == ']'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_SQRBRKT_R))
                        IdTokens.append(stateNode.LToken(tokensAndCons.TKN_SQRBRKT_R,LineN))
                        StringAux = ''
                elif (StringAux == '{'):
                        try:
                            StringAux2 = StringAux + Element[PosE+1]
                            if (StringAux2 == '{}'):
                                PosS = PosE+1
                                PosE+=1
                                TokensFounded.append(self.fillAux(StringAux2,LineN,PosS+1,PosE+1,tokensAndCons.TKN_BRKT))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_BRKT,LineN))
                                StringAux2 = ''
                                StringAux = ''
                            else:
                                PosS = PosE+1
                                TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_BRKT_L))
                                IdTokens.append(stateNode.LToken(tokensAndCons.TKN_BRKT_L,LineN))
                                StringAux = ''
                        except:
                            PosS = PosE+1
                            TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_BRKT_L))
                            IdTokens.append(stateNode.LToken(tokensAndCons.TKN_BRKT_L,LineN))
                            StringAux = ''
                elif (StringAux == '}'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_BRKT_R))
                        IdTokens.append(stateNode.LToken(tokensAndCons.TKN_BRKT_R,LineN))
                        StringAux = ''
                if(AnalizedChar==True):
                    PosE+=1
                else:
                    AnalizedChar=True
            LineN += 1
            if(OpenComment==True):
                AuxFlag = True
            if(OpenString == True):
                TokensFounded.append('***Error EOF en string*** la cadena iniciada en la línea ' + str(StringStart) + ' nunca se cierra')
                self.countError()
                OpenString = None
                LastRecognition =''
        if(OpenComment == True):
            TokensFounded.append('***Error EOF en comentario*** la cadena iniciada en la línea ' + str(CommentStart) + ' nunca se cierra')
            self.countError()
        return TokensFounded, IdTokens