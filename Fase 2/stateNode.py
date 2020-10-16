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
