import fileRW
import stateNode
#import errorManager
# variable que servira para la recuperacion de errores, se ingremetna para identificar el numero de token consumido y asi obtener la linea en el archivo
TokenQuantity = 0
class ascentParser:
    def __init__(self,tokensList):
        #reseteo del contador al iniciar para no tener problemas al momento de ejecutar varios archivos seguidamente
        TokenQuantity = 0
        Result, error = fileRW.readLRTable()
        Table = []
        if error: 
            print(error)
        else:
            #a partir del header se obtienen los simbolos terminales y no terminales
            header = Result[0].split('~')
            terminal = []
            nonterminal =[]
            #dolar es una bandera que indica la serparacion de los NT y T al encontrar '$'
            dolar = 0
            #el contador arranca en 1 debido a que el header contiene el numero de estado
            i = 1
            #contadores de simbolos
            cntTerminal = 0
            cntNonTerminal = 0
            #obteniendo simbolos terminales y no terminales
            while (i < len(header)):
                if (dolar == 0):
                    cntTerminal +=1
                    terminal.append(header[i])
                else:
                    cntNonTerminal +=1
                    nonterminal.append(header[i])
                if(header[i] =='$'):
                    dolar = 1
                i+=1
            i = 1 
            while (i < len(Result)):
                n = 0
                t = 0
                simboloT = []
                simboloNT = []
                element = Result[i].split('~')
                num = element[0]
                while (t<cntTerminal):
                    conflict = False
                    #si una acción viene vacía no se coloca en el estado
                    if (element[1+t] !='_'):
                        #se verifica que si un conflicto para el simbolo terminal
                        if('/' in element[1+t]):
                            conflict = True
                        simboloT.append(stateNode.simbol(terminal[t],element[1+t],conflict))
                    t+=1
                while (n<cntNonTerminal):
                    if (element[1+n+t] !='_'):
                        #se verifica que si un conflicto para el simbolo no terminal
                        if('/' in element[1+n+t]):
                            conflict = True
                        simboloNT.append(stateNode.simbol(nonterminal[n],element[1+n+t],conflict))
                    n+=1
                nuevo = stateNode.stateNode(num,simboloT,simboloNT)
                Table.append(nuevo)
                i+=1  
        #se obtienen las reglas de produccion de la gramática    
            productionRules = self.getProductionRules()
        
            self.evaluate(tokensList, productionRules,Table)

    def countToken(self):
        global TokenQuantity
        TokenQuantity += 1

    def evaluate(self,tokensList,productionRules,SLRTable):
        ##TokenQuantity = 0
        toknstack =[]
        for Item in tokensList:
            toknstack.append(Item.Token)
        # pila de tokens invirtiendo la tokenList para evaluar la entrada en la tabla de parseo
        tokensStack = toknstack[::-1]
        #se añade $ a la pila de tokens
        tokensStack.insert(0,'$')
        #tokensStack.reverse()
        # pila de estados
        statusStack = []
        # se añade estado inicial
        statusStack.append('0')
        # pila de simbolos reconocidos
        simbolStack = []
        while len(tokensStack) > 0:
            if ((statusStack is not None) & (simbolStack is not None) & (tokensStack is not None)):
                # se obtiene el a evaluar de la pila
                actualStatus = SLRTable[int(statusStack[-1])]
                # se evalua que el token perteneza a dicho estado
                inColection, current = self.tokenInSimbol(tokensStack[-1], actualStatus.nonterminal, actualStatus.terminal)
                if((inColection)):
                    #se evalua que no haya conflicto
                    if(current.conflict):
                        toDo = current.action.split('/')
                        current.action = toDo[0]
                        statusStack,simbolStack,tokensStack = self.doAction(current,statusStack,simbolStack,tokensStack,productionRules)
                        
                    else:
                        statusStack,simbolStack,tokensStack = self.doAction(current,statusStack,simbolStack,tokensStack,productionRules)
                else:
                    if (len(tokensList) > TokenQuantity):
                        failed = tokensList[TokenQuantity]
                        #print (errorManager.parserNotExpected(str(failed.Line),str(failed.Column),failed.Token) )
                        tokensStack.pop()
                        self.countToken()
                    else:
                        #print('Error, EOF')
                        self.countToken()
                        tokensStack.pop()
            else:
                print('Se ha producido un error' )          
                        
                    
            
    def doAction(self,current,statusStack,simbolStack,tokensStack,productionRules):
        action = current.action
        if (action[0] == 's'):
            #se apila el estado
            statusStack.append(action[1:])
            #se apila el token
            simbolStack.append(current.simbol)
            #se desapila de la entrada
            tokensStack.pop()
            self.countToken()
        elif (action[0] == 'r'): 
            # se obtiene la regla a reducir
            regla = productionRules[int(action[1:])]
            # se obtiene la cantidad de simbolos a reducir
            back = 1 
            for i in regla.right: 
                if i == ' ': 
                    back += 1
            # se comprueba que no venga epsilon (se representa como '~')
            if(regla.right not in '~'):
                #se desapila de la pila de estados
                del statusStack[-back:]
                #se desapila de la pila de simbolos
                del simbolStack[-back:]
            tokensStack.append(regla.left)
            
        elif (action.isnumeric()):
            # se apila el estado
            statusStack.append(action)
            # se apila el NT a la pila de simbolos
            simbolStack.append(tokensStack[-1])
            # se desapila el Nt de la pila de entrada
            del tokensStack[-1:]
        elif (action == 'acc'):
            if(len(tokensStack[-1]) =='$'):
                print('Error, la cadena no termino en el estado de aceptacion' )
            else:
                tokensStack.pop()
                self.countToken()
                print('La cadena ingresada es válida sintacticamente') 
        else:
            print('Se encontro una accion no valida, no cumple con el formato requerido para el archivo')
            return None, None, None

        return statusStack,simbolStack,tokensStack
        
    def tokenInSimbol(self,token,nonterminal,terminal):
        general = nonterminal + terminal 
        for element in general:
            if(token == element.simbol):
                return True, element
        return False, None
            

    def getProductionRules(self):
        Result, error = fileRW.readProductionRules()
        Rules = []
        if error: 
            print(error)
        else:
            for rule in Result:
                production = rule.split('->')
                new = stateNode.production(production[0][:-1],production[1][1:])
                Rules.append(new)
            return Rules