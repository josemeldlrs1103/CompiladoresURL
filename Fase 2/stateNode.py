#Clase para los estados
class stateNode:
    def __init__(self, state, terminal, nonterminal):
        self.state = state
        self.terminal = terminal
        self.nonterminal = nonterminal
class simbol:
    def __init__(self,simbol,action):
        self.simbol = simbol
        self.action = action