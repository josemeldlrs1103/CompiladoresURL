import tokensAndCons
class TypeVariable:
    def __init__(self, token):
        self.token = token
    def __repr__(self):
        return f'{self.token}'

class BinaryOper:
    def __init__ (self, leftOper, oper, rightOper):
        self.leftOper = leftOper
        self.oper = oper
        self.rightOper = rightOper
    def __repr__(self):
        return f'({self.leftOper}, {self.oper}, {self.rightOper})'

class UnaryOper:
    def __init__ (self, leftOper, oper):
        self.leftOper = leftOper
        self.oper = oper
    def __repr__(self):
        return f'({self.leftOper}, {self.oper})'


class ParserCls:
    def __init__(self,tokenList):
        self.tokenList = tokenList
        self.index = -1
        self.next()
    
    def next(self):
        self.index +=1
        if self.index < len(self.tokenList):
            self.currentToken = self.tokenList[self.index]
        return self.currentToken
    def back(self):
        self.index -=1
        if self.index < len(self.tokenList):
            self.currentToken = self.tokenList[self.index]
        return self.currentToken
    

    ### reglas de produccion ###
    def ProgramVoid(self):
        self.DeclVoid()
        self.ProgramVoid_Prime()

    def DeclVoid(self):
        #si hay tokens por evaluar
        self.DeclVoid_Prime()
        #si no terminar ejecucion

    def DeclVoid_Prime(self):  

        #tratar de avanzar en lista hasta encontrar putno y coma
        if self.currentToken in (tokensAndCons.TKN_SEMICOLON):
           self.VariableDeclVoid()
        #tratar de avanzar en lista hasta encontrar un '('
        elif self.currentToken in (tokensAndCons.TKN_PAREN_L):
            self.FunctionDeclareVoid()
        ## si ya no hay mas tokens muere
        ## si no vuelve a DeclVoid
        self.DeclVoid()

    def VariableDeclVoid(self):
        k = 0
    def FunctionDeclareVoid(self):
        k = 0
    def ProgramVoid_Prime(self):
        k = 0
        #if tokens irse a programVoid
        #si no se detecta epsilon
        


    def TypeR (self):
        token = self.currentToken
        if token in (tokensAndCons.TKN_INT, tokensAndCons.TKN_DOUBLE, tokensAndCons.TKN_BOOLEAN, tokensAndCons.TKN_STRING, tokensAndCons.TKN_IDENTIFIER):
            self.next()
            return TypeVariable(token)
    
