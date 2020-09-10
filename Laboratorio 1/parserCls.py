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
    

    ### reglas de produccion ###
    #def TypeR (self):
        #token = self.currentToken
        #if token in (tokensAndCons.TKN_INT, tokensAndCons.TKN_DOUBLE, tokensAndCons.TKN_BOOLEAN, tokensAndCons.TKN_STRING, tokensAndCons.TKN_IDENTIFIER):
            #self.next()
            #return TypeVariable(token)