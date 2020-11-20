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
   def __init__(self,Token,Name,Value,Line,StartCol,EndCol):
        self.Token = Token
        self.Name = Name
        self.Value = Value
        self.Line = Line
        self.Column = 'Col: '+ str(StartCol) + ' - ' + str(EndCol)
#Clase para la TS
class elementTS:
    def __init__(self,Token,Type,Name,Value,Line,Column):
        self.Token = Token
        self.Type = Type
        self.Name = Name
        self.Value = Value
        self.Line = Line
        self.Column = Column
