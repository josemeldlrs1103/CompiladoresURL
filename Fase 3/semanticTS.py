import stateNode
import tokensAndCons
import os
# global para registro de errores
errors = []
class semanticTS:
    def __init__(self,tokensList,Texto):
        TS = []
        TSLog = []
        previous = None
        previousP = None
        toMod = None
        funcToMod = None
        newVal = []
        valFunc = []
        ableToSearch = ['int','double','bool','string','const']
        ##se añaden todos los tokens a la la TS
        Const = False
        for element in tokensList:
            if((previous is not None) and (previous.Name in ableToSearch) and toMod is None):
                # se verifica que el token sea apto para añadirlo a la TS
                if (element.Token in tokensAndCons.AbleToTS and element.Name not in tokensAndCons.excludedName):
                    # se añade la declaración
                    TS.append(stateNode.elementTS(element.Token, previous.Name ,element.Name, element.Value, Const,element.Line,element.Column,1))
                    TSLog.append(stateNode.elementTS(element.Token, previous.Name ,element.Name, element.Value, Const,element.Line,element.Column,1))
                    if(element.Token == tokensAndCons.TKN_IDENTIFIER):
                        # se añade el identificador a los permitidos
                        ableToSearch.append(str(element.Name))
                        #si se encuentra una asignacion se obtendra su valor
                elif (element.Token in tokensAndCons.TKN_EQUALS):
                    if (previous.Name in ableToSearch):
                        # se obtiene el nombre del simbolo al que se modificara su valor
                        toMod = previous.Name
                elif ((element.Token in tokensAndCons.TKN_PAREN_L) and (previous.Token in tokensAndCons.TKN_IDENTIFIER) and (previousP.Token in tokensAndCons.AbleToTS)):
                    funcToMod = previous.Name
                    
                elif ((previous.Token in tokensAndCons.TKN_RETURN) and (element.Token in ableToSearch)):
                    valFunc.append(element.Token)

            elif ((toMod is not None) and (element.Token not in tokensAndCons.TKN_SEMICOLON)):
                #se concatena el nuevo valor hasta encontrar un punto y coma
                if(element.Name in ableToSearch):
                    searchT = True
                    i=0
                    while(searchT and i < len(TS)):
                        if(TS[i].Name == element.Name):
                            if(TS[i].Token == element.Token):
                                #se obtiene el valor para dicho simbolo
                                newVal.append(TS[i].Value)
                                searchT = False
                            else:
                                newVal.append('Los tipos no coinciden')
                                searchT = False
                        i+=1
                else:
                    newVal.append(element.Value)
            elif ((funcToMod is not None) and (previous.Token in tokensAndCons.TKN_RETURN)):
                #se busca el simbolo a modificar
                i = 0
                valorValor = None
                while (valorValor is None and i< len(TS)):
                    if(TS[i].Name == element.Name):
                        valorValor = self.getValue(TS[i].Value, TS[i].Type)
                    i += 1
                i = 0
                while (funcToMod is not None) and  i < len(TS):
                    if(TS[i].Name == funcToMod and TS[i].Mod == 1):
                        #se obtiene el valor para dicho simbolo
                        TS[i].Value = 'La función retorna: ' + self.getValue(valorValor, TS[i].Type)
                        TSLog.append(TS[i])
                        funcToMod = None
                        valFunc =[]
                    i+=1
            elif ((toMod is not None) and (element.Token in tokensAndCons.TKN_SEMICOLON)):
                #se busca el simbolo a modificar
                i = 0
                while (toMod is not None) and  i < len(TS):
                    if(TS[i].Name == toMod and TS[i].Mod == 1):
                        #se obtiene el valor para dicho simbolo
                        TS[i].Value = self.getValue(newVal, TS[i].Type)
                        TSLog.append(TS[i])
                        if(TS[i].Const == True):
                            TS[i].Mod = 0
                        
                        toMod = None
                        
                        newVal =[]
                    i+=1
            elif((previous is not None) and (element.Token not in tokensAndCons.TKN_IDENTIFIER)and (element.Name not in ableToSearch) and len(ableToSearch)>5 and (element.Name not in tokensAndCons.excludedName and element.Token in tokensAndCons.TKN_IDENTIFIER )):
                    errors.append('El elemento ' + element.Name +' no ha sido declarado previamente')  
                    print ('El elemento ' + element.Name +' no ha sido declarado previamente')  
            if((previous is not None) and (previous.Name == 'const')):
                Const = True
            else:
                Const = False
            previousP = previous
            previous = element
        if TS is not None:
            SymbolT = []
            Historial = []
            #Definición de los campos de la tabla
            SymbolT.append("Nombre|Tipo|Valor|Linea|Espacio columna")
            Historial.append("Nombre|Tipo|Valor|Linea|Espacio columna")
            #agregando las líneas a imprimir en la tabla
            for Variable in TS:
                if (Variable.Const == True):
                    NuevoTipo = "Const"+Variable.Type
                    if (Variable.Value != None):
                        SymbolT.append(str(Variable.Name)+"|"+ str(NuevoTipo)+"|"+ str(Variable.Value)+"|"+ str(Variable.Line)+"|"+str(Variable.Column))
                    else:
                        SymbolT.append(str(Variable.Name)+"|"+ str(NuevoTipo)+"|"+ "Null"+"|"+ str(Variable.Line)+"|"+str(Variable.Column))
                else:
                    if (Variable.Value != None):
                        SymbolT.append(str(Variable.Name)+"|"+ str(Variable.Type)+"|"+ str(Variable.Value)+"|"+ str(Variable.Line)+"|"+str(Variable.Column))
                    else:
                        SymbolT.append(str(Variable.Name)+"|"+ str(Variable.Type)+"|"+ "Null"+"|"+ str(Variable.Line)+"|"+str(Variable.Column))
            for Registro in TSLog:
                if (Registro.Const == True):
                    NuevoTipo = "Const"+Registro.Type
                    if (Registro.Value != None):
                        Historial.append(str(Registro.Name)+"|"+ str(NuevoTipo)+"|"+ str(Registro.Value)+"|"+ str(Registro.Line)+"|"+str(Registro.Column))
                    else:
                        Historial.append(str(Registro.Name)+"|"+ str(Registro)+"|"+ "Null"+"|"+ str(Registro.Line)+"|"+str(Registro.Column))
                else:
                    if (Registro.Value != None):
                        Historial.append(str(Registro.Name)+"|"+ str(Registro.Type)+"|"+ str(Registro.Value)+"|"+ str(Registro.Line)+"|"+str(Registro.Column))
                    else:
                         Historial.append(str(Registro.Name)+"|"+ str(Registro.Type)+"|"+ "Null"+"|"+ str(Registro.Line)+"|"+str(Registro.Column))
            file = open(os.path.splitext(Texto)[0] + ".out", "w")
            file.write("----------Historial----------\n")
            for linea in Historial:
                file.write(linea+"\n")
            if(errors is not None):
                for er in errors:
                    file.write(er + "\n")
            file.write("----------Tablafinal----------\n")
            for linea in SymbolT:
                file.write(linea+"\n")
            file.close()
            print('La tabla de simbolos obtenida es la siguiente:\n')
            for linea in SymbolT:
                print(linea+"\n")


    def getValue(self,newVal,Type):
        #se evalua que el tipo que viene sea valido
        if (Type == 'int' and newVal[0].isnumeric()):
            toBack = 0
            toDo = ''
            for item in newVal:
                if (item is not None):
                    if (toDo == ''):
                        if(item == '+' or item == '-' or item == '*' or item == '/' or item == '%'):
                            toDo = item
                        else:
                            toBack += int(item)
                    else:
                        if(item.isnumeric()):
                            if (toDo == '+'):
                                toDo = ''
                                toBack += int(item)
                            elif(toDo == '-'):
                                toDo = ''
                                toBack -= int(item)
                            elif(toDo == '*'):
                                toDo = ''
                                toBack *= int(item)
                            elif(toDo == '/'):
                                toDo = ''
                                toBack /= int(item)
                            elif(toDo == '%'):
                                toDo = ''
                                toBack %= int(item)
                            else:
                                errors.append('Se encontró un operador no valido para int: ' + str(toDo))
                                return 'Se encontró un operador no valido para int: ' + str(toDo)
                        else:
                            errors.append('Error de tipos en variable, se trató de emparejar ' + str(Type) +' y ' +str(self.getTypeForVal(item)))
                            return 'Error de tipos en variable, se trató de emparejar ' + str(Type) +' y ' +str(self.getTypeForVal(item))
            return str(toBack)
        elif (Type == 'double'):
            if( '.' in newVal[0]):
                toBack = 0
                toDo = ''
                if(type(newVal) is list):
                    for item in newVal:
                        if (toDo == ''):
                            if(item == '+' or item == '-' or item == '*' or item == '/' or item == '%'):
                                toDo = item
                            else:
                                toBack += float(item)
                        else:
                            # se permite sumar un float y un int para los datos double
                            if('.' in item or item.isnumeric()):
                                if (toDo == '+'):
                                    toDo = ''
                                    toBack += float(item)
                                elif(toDo == '-'):
                                    toDo = ''
                                    toBack -= float(item)
                                elif(toDo == '*'):
                                    toDo = ''
                                    toBack *= float(item)
                                elif(toDo == '/'):
                                    toDo = ''
                                    toBack /= float(item)
                                elif(toDo == '%'):
                                    toDo = ''
                                    toBack %= float(item)
                                else:
                                    errors.append('Se encontró un operador no valido para double: ' + str(toDo))
                                    return 'Se encontró un operador no valido para double: ' + str(toDo)
                            else:
                                errors.append('Error de tipos en variable, se trató de emparejar ' + str(Type) +' y ' +str(self.getTypeForVal(item)))
                                return 'Error de tipos en variable, se trató de emparejar ' + str(Type) +' y ' +str(self.getTypeForVal(item))
                else:
                    toBack = float(newVal)
            else:
                toBack = float(newVal)
            return str(toBack)
        elif (Type == 'bool'):
            toBack = ''
            toDo = ''
            if(type(newVal) is list):
                if (newVal[0] == 'false' or newVal[0] == 'true' or newVal[0] == 'null'):
                    for item in newVal:
                        if (toDo == ''):
                            if(item == '&&' or item == '||' or item == '!'):
                                toDo = item
                            else:
                                toBack += item
                        elif(item == 'false' or item == 'true'):
                            if(toDo =='&&'):
                                if toBack == item:
                                    toDo = ''
                                    toBack = 'true'
                                else: 
                                    toDo = ''
                                    toBack = 'false'
                            elif(toDo =='||'):
                                if (toBack == 'true' or item == 'true'):
                                    toDo = ''
                                    toBack = 'true'
                                else: 
                                    toDo = ''
                                    toBack = 'false'
                            elif(toDo =='!'):
                                if(item == 'true'):
                                    toDo =''
                                    toBack = 'false'
                                elif(item == 'false'):
                                    toDo =''
                                    toBack = 'true'
                                else:
                                    return 'la negación no es valida'
                            else:
                                errors.append('Se encontró un operador no valido para bool: ' + str(toDo))
                                return 'Se encontró un operador no valido para bool: ' + str(toDo)
                        elif(item == 'null'):
                            toDo = ''
                            toBack = 'null'
                else:
                    return 'valor no valido para bool'
            else:
                toBack += newVal 
            return toBack
            
        elif (Type == 'string'  and '"' in newVal[0]):
            toBack = ''
            toDo = ''
            if(type(newVal) is list):
                for item in newVal:
                    if (toDo == ''):
                        if(item == '+'):
                            toDo = item 
                        elif('"' in item):
                            toDo = ''
                            toBack+=item
                        elif(item.isalpha()):
                            toBack+=item
                        else:
                            errors.append('Se encontró un operador no valido para string: ' + str(toDo))
                            return 'Se encontró un operador no valido para string: ' + str(toDo)
                    else:
                        toDo =''
                        toBack += item
            else:
                toBack += newVal
            return '"'+toBack.replace('"','') + '"'
        else:
            errors.append('Error de tipos en variable, se trató de emparejar ' + str(Type) +' y ' +str(self.getTypeForVal(newVal)))
            return 'Error de tipos en variable, se trató de emparejar ' + str(Type) +' y ' +str(self.getTypeForVal(newVal))

    def getTypeForVal(self,newVal):
        for item in newVal:
            if (item.isnumeric()):
                return 'int'
            elif('.' in item):
                return 'double'
            elif('"' in item):
                return 'string'
            elif (item == 'false' or item == 'true' or item == 'null'):
                return 'bool'
            else:
                return 'tipo desconocido'
