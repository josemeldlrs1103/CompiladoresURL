import stateNode
import tokensAndCons
class semanticTS:
    def __init__(self,tokensList):
        TS = []
        previous = None
        toMod = None
        newVal = []
        ableToSearch = ['int','double','bool','string','const']
        ##se añaden todos los tokens a la la TS
        for element in tokensList:
            if((previous is not None) and (previous.Name in ableToSearch) and toMod is None):
                # se verifica que el token sea apto para añadirlo a la TS
                if (element.Token in tokensAndCons.AbleToTS and element.Name not in tokensAndCons.excludedName):
                    # se añade la declaración
                    TS.append(stateNode.elementTS(element.Token, previous.Name ,element.Name, element.Value, element.Line,element.Column))
                    if(element.Token == tokensAndCons.TKN_IDENTIFIER):
                        # se añade el identificador a los permitidos
                        ableToSearch.append(str(element.Name))
                        #si se encuentra una asignacion se obtendra su valor
                elif (element.Token in tokensAndCons.TKN_EQUALS):
                    if (previous.Name in ableToSearch):
                        # se obtiene el nombre del simbolo al que se modificara su valor
                        toMod = previous.Name
            elif ((toMod is not None) and (element.Token not in tokensAndCons.TKN_SEMICOLON)):
                #se concatena el nuevo valor hasta encontrar un punto y coma
                newVal.append(element.Value)
            elif ((toMod is not None) and (element.Token in tokensAndCons.TKN_SEMICOLON)):
                #se busca el simbolo a modificar
                i = 0
                while (toMod is not None):
                    if(TS[i].Name == toMod):
                        #se obtiene el valor para dicho simbolo
                        TS[i].Value = self.getValue(newVal, TS[i].Type)
                        toMod = None
                        newVal =[]
                    i+=1
            previous = element

        print('debug')

    def getValue(self,newVal,Type):
        #se evalua que el tipo que viene sea valido
        if (Type == 'int' and newVal[0].isnumeric()):
            toBack = 0
            toDo = ''
            for item in newVal:
                if (toDo == ''):
                    if(item == '+' or item == '-' or item == '*' or item == '/' or item == '%'):
                        toDo = item
                    else:
                        toBack += int(item)
                else:
                    if (toDo == '+'):
                        toBack += int(item)
                    elif(toDo == '-'):
                        toBack -= int(item)
                    elif(toDo == '*'):
                        toBack *= int(item)
                    elif(toDo == '/'):
                        toBack /= int(item)
                    elif(toDo == '%'):
                        toBack %= int(item)
                    else:
                        return 'operador no valido para int'
            return str(toBack)
        elif (Type == 'double'  and '.' in newVal[0]):
            toBack = 0
            toDo = ''
            for item in newVal:
                if (toDo == ''):
                    if(item == '+' or item == '-' or item == '*' or item == '/' or item == '%'):
                        toDo = item
                    else:
                        toBack += float(item)
                else:
                    if (toDo == '+'):
                        toBack += float(item)
                    elif(toDo == '-'):
                        toBack -= float(item)
                    elif(toDo == '*'):
                        toBack *= float(item)
                    elif(toDo == '/'):
                        toBack /= float(item)
                    elif(toDo == '%'):
                        toBack %= float(item)
                    else:
                        return 'operador no valido para double'
            return str(toBack)
        elif (Type == 'bool'):
            if (newVal[0] == "false" or newVal[0] == "true"):
                return newVal[0]
            else:
                return "valor no valido para bool"
        elif (Type == 'string'  and '"' in newVal[0]):
            toBack = ''
            toDo = ''
            for item in newVal:
                if (toDo == ''):
                    if(item == '+'):
                        toDo = item 
                    elif('"' in item):
                        toBack+=item
                    else:
                        return 'operador no valido para string'
                else:
                    toBack += item
            return '"'+toBack.replace('"','') + '"'
        else:
            return 'error de tipos'       