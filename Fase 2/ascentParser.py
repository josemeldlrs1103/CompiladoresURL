import fileRW
import stateNode

class ascentParser:
    def __init__(self,tokensList):
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

    def evaluate(self,tokensList,productionRules,SLRTable):
        # pila de tokens invirtiendo la tokenList para evaluar la entrada en la tabla de parseo
        tokensStack = tokensList[::-1]
        #se añade $ a la pila de tokens
        tokensStack.insert(0,'$')
        #tokensStack.reverse()
        # pila de estados
        statusStack = []
        # se añade estado inicial
        statusStack.append('0')
        # pila de simbolos reconocidos
        simbolStack = []
        for token in tokensList:
            # se obtiene el a evaluar de la pila
            actualStatus = SLRTable[int(statusStack[-1])]
            # se evalua que el token perteneza a dicho estado
            inColection, current = self.tokenInSimbol(token, actualStatus.nonterminal, actualStatus.terminal)
            if(inColection):
                #se evalua que no haya conflicto
                if(current.conflict):
                    print('se presento un conflicto') 
                else:
                    action = current.action
                    if (action[0] == 's'):
                        #se apila el estado
                        statusStack.append(action[1:])
                        #se apila el token
                        simbolStack.append(current.simbol)
                        #se desapila de la entrada
                        tokensStack.pop()
                        print('desplazamiento')
                    elif (action[0] == 'r'): 
                        print('reducicion')
                    elif (action == 'acc'):
                        print('aceptado')
                    elif (isinstance(action, int)):
                        print('ir a ')
                    else:
                        print('accion no valida')
                    
            else:
                print('error')
            

    def tokenInSimbol(self,token,nonterminal,terminal):
        general = nonterminal + terminal 
        for element in general:
            if(token == element.simbol):
                return True, element
        return False
            

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