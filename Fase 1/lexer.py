import tokensAndCons
import re
import errorManager
ErrorQuantity = 0
class Lexer:

    def __init__(self,Text):
        self.Text = Text
    
    def fillAux (self, token, line, colStart, colEnd, tokenID):
        result = token + ' línea ' + str(line) + ' col ' + str(colStart) + '-' +str(colEnd) + ' es: ' + tokenID
        return result

    def countError(self):
        global ErrorQuantity
        ErrorQuantity += 1
    


    def EvaluateLines(self):
        TokensFounded=[]
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
                elif(re.search(tokensAndCons.Reservadas2,StringAnalizer)):
                    AnalizedChar = True
                    LastRecognition='Reservada'
                    Prior = True
                elif(re.search(tokensAndCons.Identificadores,StringAnalizer)):
                        AnalizedChar =True
                        LastRecognition = 'Identificador'
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
                    AnalizedChar = True
                    LastRecognition = 'Inicio dob'
                elif(re.search(tokensAndCons.StringStep1,StringAnalizer)):
                    OpenString = True
                    LastRecognition = 'String'
                    StringStart = LineN
                elif(re.search(tokensAndCons.StringStep2,StringAnalizer)):
                    OpenString = False
                    LastRecognition = 'String'
                elif(re.search(tokensAndCons.OneLineCommentsStep1, StringAnalizer)):
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
                    LastRecognition = 'Multi-Line Comment'
                elif(re.search(tokensAndCons.MultiLineCommentsStep3, StringAnalizer)):
                    LastRecognition = 'Multi-Line Comment'
                    OpenComment = False
                    StringAnalizer = ''
                    AuxFlag = False
                elif(re.search(tokensAndCons.ExtraCaseComment,StringAnalizer)):
                    StringAnalizer = StringAnalizer[0:2]
                    if(StringAux=='*' and Element[PosE+1]=='/'):
                        StringAnalizer += Element[PosE]
                else:
                    if(len(StringAnalizer)>1 and LastRecognition!=''):
                        if(StringAnalizer!='\n'):
                            StringAnalizer = StringAnalizer[:-1]
                        if( LastRecognition == 'Reservada'):
                            if(Prior == True):
                                if(StringAux in ' \n\t'):
                                    StringAnalizer += Element[PosE]
                                TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_'+LastRecognition))
                                Prior=False
                                if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                                    AnalizedChar = False
                        elif(LastRecognition == 'Identificador'):
                            if(DiscardChars==False):
                                TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_'+LastRecognition))
                            if(StringAux!='' and StringAux!=' ' and StringAux!='\t' and StringAux!='\n' and StringAux!='+' and StringAux!='-' and StringAux!='*' and StringAux!='/' and StringAux!='%' and StringAux!='<' and StringAux!='>' and StringAux!='=' and StringAux!='!' and StringAux!='&' and StringAux!='|' and StringAux!=';' and StringAux!=',' and StringAux!='.' and StringAux!='(' and StringAux!=')' and StringAux!='[' and StringAux!=']' and StringAux!='{' and StringAux!='}'):
                                DiscardChars = True
                            else:
                                DiscardChars = False
                                LastRecognition = ''
                        elif(LastRecognition == 'Booleano'):
                            TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_Boolean con el valor: '+StringAnalizer))
                            if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                                 AnalizedChar = False
                        elif(LastRecognition == 'Integer'):
                            TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_Int con el valor: '+StringAnalizer))
                            if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                                AnalizedChar = False
                        elif(LastRecognition == 'Double'):
                            TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_Double con el valor: '+StringAnalizer))
                            if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                                AnalizedChar = False
                        elif(LastRecognition == 'Inicio Hex' or LastRecognition == 'Inicio dob'):
                            TokensFounded.append(errorManager.incomplete(LineN,StringAnalizer))
                            self.countError()
                            if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                                AnalizedChar = False
                    else:
                        if(StringAux not in ' \n\t+-*/%<>=!&|;,.()[]}{'):
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
                    TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_'+LastRecognition))
                    Prior=False
                    StringAnalizer=''
                if (StringAux == '\n'):
                    if(StringAnalizer!='\n'):
                        StringAnalizer = StringAnalizer[:-1]
                    if( LastRecognition == 'Reservada'):
                            if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                                TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_'+LastRecognition))
                                AnalizedChar = False
                    elif(LastRecognition == 'Identificador'):
                        if(DiscardChars==False):
                            TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_'+LastRecognition))
                            if(StringAux!='' and StringAux!=' ' and StringAux!='\t' and StringAux!='\n' and StringAux!='+' and StringAux!='-' and StringAux!='*' and StringAux!='/' and StringAux!='%' and StringAux!='<' and StringAux!='>' and StringAux!='=' and StringAux!='!' and StringAux!='&' and StringAux!='|' and StringAux!=';' and StringAux!=',' and StringAux!='.' and StringAux!='(' and StringAux!=')' and StringAux!='[' and StringAux!=']' and StringAux!='{' and StringAux!='}'):
                                DiscardChars = True
                            else:
                                DiscardChars = False
                                LastRecognition = ''
                    elif(LastRecognition == 'Booleano'):
                        if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                            TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_Boolean con el valor: '+StringAnalizer))
                            AnalizedChar = False
                    elif(LastRecognition == 'Integer'):
                        if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                            TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_Int con el valor: '+StringAnalizer))
                            AnalizedChar = False
                    elif(LastRecognition == 'Double'):
                        if(StringAnalizer!='' and StringAnalizer!=' ' and StringAnalizer!='\t' and StringAnalizer!='\n' and StringAnalizer!='+' and StringAnalizer!='-' and StringAnalizer!='*' and StringAnalizer!='/' and StringAnalizer!='%' and StringAnalizer!='<' and StringAnalizer!='>' and StringAnalizer!='=' and StringAnalizer!='!' and StringAnalizer!='&' and StringAnalizer!='|' and StringAnalizer!=';' and StringAnalizer!=',' and StringAnalizer!='.' and StringAnalizer!='(' and StringAnalizer!=')' and StringAnalizer!='[' and StringAnalizer!=']' and StringAnalizer!='{' and StringAnalizer!='}'):
                            TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_Double con el valor: '+StringAnalizer))
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
                        TokensFounded.append(self.fillAux(StringAnalizer,LineN,PosS+1,PosE,'T_String con el valor: '+StringAnalizer))
                    else:
                        TokensFounded.append('Error encontrado en línea ' + LineN + ', la cadena presente en la línea contiene un caracter no válido')
                        self.countError()
                    StringAnalizer = ''
                    OpenString = None
                if(LastRecognition == 'String' or LastRecognition == 'Comment Line' or LastRecognition == 'Multi-Line Comment'):
                    StringAux =''
                if (StringAux == '+'):
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
                elif (StringAux == ';'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_SEMICOLON))
                        StringAux = ''
                elif (StringAux == ','):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_COMMA))
                        StringAux = ''
                elif (StringAux == '.'):
                    if(DecimalExist== False):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_DOT))
                        StringAux = ''
                elif (StringAux == '('):
                    
                        if (re.search(tokensAndCons.ERParentesis, Element)):
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
                        else:
                            PosS = PosE+1
                            TokensFounded.append(errorManager.expected(LineN,PosS+1, '(', ')'))
                            self.countError()
                            StringAux = ''
                elif (StringAux == ')'):
                        PosS = PosE+1
                        TokensFounded.append(self.fillAux(StringAux,LineN,PosS+1,PosE+1,tokensAndCons.TKN_PAREN_R))
                        StringAux = ''
                elif (StringAux == '['):
                        if (re.search(tokensAndCons.ERCorchetes, Element)):
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
                        else:
                            PosS = PosE+1
                            TokensFounded.append(errorManager.expected(LineN,PosS+1, '[', ']'))
                            self.countError()
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
        if(OpenComment == True):
            TokensFounded.append('***Error EOF en comentario*** la cadena iniciada en la línea ' + str(CommentStart) + ' nunca se cierra')
            self.countError()
        return TokensFounded