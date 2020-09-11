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
        if self.index < len(self.tokenList):        
            self.DeclVoid()
            self.ProgramVoid_Prime()

    def ProgramVoid_Prime(self):
        if self.index < len(self.tokenList):        
            self.next()
            #se vuelve a program ya que aun hay elementos en la lista de tokens
            self.ProgramVoid()
        else:
            #se detecta epsilon
            return

    def DeclVoid(self):
        if self.index < len(self.tokenList):        
            self.DeclVoid_Prime()
            self.DeclVoid()
        
    def DeclVoid_Prime(self):
        if self.index < len(self.tokenList): 
            # se crea un token temporal para evaluar que venga un ';'       
            tempToken = self.tokenList[self.index + 2]
            if tempToken in (tokensAndCons.TKN_SEMICOLON):
                self.VariableDeclVoid()
            elif tempToken in (tokensAndCons.TKN_PAREN_L):
                self.FunctionDeclVoid()
    def FunctionDeclVoid(self):
        self.FunctionDeclVoid_Prime()

    def FunctionDeclVoid_Prime(self):
        self.FunctionTypeVoid()

    def FunctionTypeVoid(self):
        token = self.currentToken
        # se evalua que la función tenga un tipo
        if token in (tokensAndCons.TKN_INT, tokensAndCons.TKN_DOUBLE, tokensAndCons.TKN_BOOLEAN, tokensAndCons.TKN_STRING, tokensAndCons.TKN_IDENTIFIER):
            self.next()
            self.TypeVoid()
        # se evalua que venga un void
        elif token in (tokensAndCons.TKN_VOID):
            self.next()
            token = self.currentToken
            # se evalua que siga un identificador
            if token in (tokensAndCons.TKN_IDENTIFIER):
                self.next()
                token = self.currentToken
                # se evalua que siga un '('
                if token in (tokensAndCons.TKN_PAREN_L):
                    self.next()
                    self.FormalsVoid()
                    if token in (tokensAndCons.TKN_PAREN_R):
                        self.next()
                        self.StmtVoid()
            #else error  
    def StmtVoid(self):
        token = self.currentToken
        if token in (tokensAndCons.TKN_WHILE):
            self.next()
            self.WhileStmtVoid()
        elif token in (tokensAndCons.TKN_IF):
            self.next()
            self.IfStmtVoid()
        #este bloque define si el stmt es o no epsilon, ya que al no coincidir con ninguno de los simbolos terminales qen los que puede derivar
        #Expr se detecta que se tiene una cadena vacia 
        elif token in (tokensAndCons.TKN_INTCONST, tokensAndCons.TKN_DOUBCONST, tokensAndCons.TKN_BOOLCONST,tokensAndCons.TKN_STRCONST, tokensAndCons.TKN_NULL,
                       tokensAndCons.TKN_OR, tokensAndCons.TKN_AND,tokensAndCons.TKN_DBLEQLS, tokensAndCons.TKN_DISTINCT, tokensAndCons.TKN_MINOR, tokensAndCons.TKN_MAJOR,
                       tokensAndCons.TKN_MAJEQLS, tokensAndCons.TKN_MINEQLS, tokensAndCons.TKN_PLUS, tokensAndCons.TKN_MINUS, tokensAndCons.TKN_MULT, tokensAndCons.TKN_DIV,
                       tokensAndCons.TKN_PRCTGE, tokensAndCons.TKN_EXCMARK, tokensAndCons.TKN_PAREN_L, tokensAndCons.TKN_IDENTIFIER):
            self.ExprVoid()

    def WhileStmtVoid(self):
        token = self.currentToken()
        if token in (tokensAndCons.TKN_PAREN_L):
            #se avanza y mueve a EXPR
            self.next()
            self.ExprVoid()
            if token in (tokensAndCons.TKN_PAREN_R):
                #se avanza y mueve a stmt
                self.next()
                self.StmtVoid()

    def IfStmtVoid(self):
        token = self.currentToken()
        if token in (tokensAndCons.TKN_PAREN_L):
            #se avanza y mueve a EXPR
            self.next()
            self.ExprVoid()
            if token in (tokensAndCons.TKN_PAREN_R):
                #se avanza y mueve a stmt
                self.next()
                self.StmtVoid()
                self.next()
                self.IfStmtVoid_Prime()

    def IfStmtVoid_Prime(self):
        token = self.currentToken()
        if token in (tokensAndCons.TKN_ELSE):
            #si viene un else se vuelve a stmt
            self.StmtVoid ()

        
    def ExprVoid(self):
        token = self.currentToken()

    def ConstantVoid(self):
        token = self.currentToken()
        if token in (tokensAndCons.TKN_INTCONST, tokensAndCons.TKN_DOUBCONST, 
                     tokensAndCons.TKN_BOOLCONST,tokensAndCons.TKN_STRCONST, tokensAndCons.TKN_NULL):
            self.next()

    def FormalsVoid(self):
        self.VariableVoid()
        self.FormalsVoid_Prime()

    def FormalsVoid_Prime(self):
        self.next()
        token = self.currentToken
        if token in (tokensAndCons.TKN_SEMICOLON):
            self.next()
            self.VariableVoid()
            self.FormalsVoid_Prime()

    def VariableDeclVoid(self):
        self.VariableVoid()
    
    def VariableVoid(self):
        self.TypeArrayVoid()


    def TypeArrayVoid(self):
        self.TypeVoid()
        #se evalua que despues de el tipo venga un identificador
        token = self.currentToken
        if token in (tokensAndCons.TKN_IDENTIFIER):
            self.next()
            token = self.currentToken
        if token in (tokensAndCons.TKN_SEMICOLON):
            self.next()

    def TypeVoid(self):
        token = self.currentToken
        if token in (tokensAndCons.TKN_INT, tokensAndCons.TKN_DOUBLE, tokensAndCons.TKN_BOOLEAN, tokensAndCons.TKN_STRING, tokensAndCons.TKN_IDENTIFIER):
            self.next()
            self.ArrayVoid()

    def ArrayVoid(self):
        token = self.currentToken
        if token in (tokensAndCons.TKN_SQRBRKT):
            self.next()
        ## si no se detecta como epsilon y no se avanza 
  
