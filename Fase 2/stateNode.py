#Clase para los estados
class stateNode:
    def __init__(self, state, terminal, nonterminal):
        self.state = state
        self.terminal = terminal
        self.nonterminal = nonterminal

class simbol:
    def __init__(self,simbol,action,conflict):
        self.simbol = simbol
        self.action = action
        self.conflict = conflict
#clase para las reglas de produccion
class production:
    def __init__(self,left,right):
        self.left = left
        self.right = right
#Clase para almacenar los tokens y la lína a la que corresponden
class LToken:
    def __init__(self,Token,Line,StartCol,EndCol):
        self.Token = Token
        self.Line = Line
        self.Column = 'Col: '+ str(StartCol) + ' - ' + str(EndCol)