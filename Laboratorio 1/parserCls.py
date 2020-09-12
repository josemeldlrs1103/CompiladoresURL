import tokensAndCons
import sys
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
        self.error = 0
    
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
        if (self.error == 0):
            return 'El archivo no cuenta con errores'
        else:
            return 'El archivo cuenta con errores'

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
            else:
                self.error+=1
                sys.exit()


    def FunctionDeclVoid(self):
        self.FunctionDeclVoid_Prime()
        token = self.currentToken
        if token in (tokensAndCons.TKN_IDENTIFIER):
            self.next()
            token = self.currentToken
            if token in (tokensAndCons.TKN_PAREN_L):
                self.next()
                self.FormalsVoid()
                token = self.currentToken
                if token in (tokensAndCons.TKN_PAREN_R):
                    self.next()
                    self.StmtVoid()

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
        else:
            self.error+=1
            sys.exit()
 
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
        elif token in (tokensAndCons.TKN_INTCONST, tokensAndCons.TKN_DOUBCONST, tokensAndCons.TKN_BOOLCONST,tokensAndCons.TKN_STRCONST, tokensAndCons.TKN_NULL, tokensAndCons.TKN_OR, tokensAndCons.TKN_AND,tokensAndCons.TKN_DBLEQLS, tokensAndCons.TKN_DISTINCT, tokensAndCons.TKN_MINOR, tokensAndCons.TKN_MAJOR, tokensAndCons.TKN_MAJEQLS, tokensAndCons.TKN_MINEQLS, tokensAndCons.TKN_PLUS, tokensAndCons.TKN_MINUS, tokensAndCons.TKN_MULT, tokensAndCons.TKN_DIV, tokensAndCons.TKN_PRCTGE, tokensAndCons.TKN_EXCMARK, tokensAndCons.TKN_PAREN_L, tokensAndCons.TKN_IDENTIFIER, tokensAndCons.TKN_INT, tokensAndCons.TKN_DOUBLE, tokensAndCons.TKN_STRING, tokensAndCons.TKN_BOOLEAN):
            self.ExprVoid()
            ##agregar validación ;
        else:
            self.error+=1
            sys.exit()

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
        else:
            self.error+=1
            sys.exit()

    def IfStmtVoid(self):
        token = self.currentToken
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
        else:
            self.error+=1
            sys.exit()

    def IfStmtVoid_Prime(self):
        token = self.currentToken()
        if token in (tokensAndCons.TKN_ELSE):
            self.next()
            #si viene un else se vuelve a stmt
            self.StmtVoid ()

        
    def ExprVoid(self):
        token = self.currentToken
        #evaluar constantes:
        if token in (tokensAndCons.TKN_INTCONST, tokensAndCons.TKN_DOUBCONST, tokensAndCons.TKN_BOOLCONST,tokensAndCons.TKN_STRCONST, tokensAndCons.TKN_NULL, tokensAndCons.TKN_INT, tokensAndCons.TKN_DOUBLE, tokensAndCons.TKN_STRING, tokensAndCons.TKN_BOOLEAN):
            self.next()
        #evaluar this:
        elif token in (tokensAndCons.TKN_THIS):
            self.next()
        #evaluar new(ident);
        elif token in (tokensAndCons.TKN_NEW):
            self.next()
            token = self.currentToken()
            if token in (tokensAndCons.TKN_PAREN_L):
                self.next()
                token = self.currentToken()
                if token in (tokensAndCons.TKN_IDENTIFIER):
                    self.next()
                    token = self.currentToken()
                    if token in (tokensAndCons.TKN_PAREN_R):
                        self.next()
        #ExprOr
        elif token in (tokensAndCons.TKN_OR, tokensAndCons.TKN_AND,tokensAndCons.TKN_DBLEQLS, tokensAndCons.TKN_DISTINCT, tokensAndCons.TKN_MINOR, tokensAndCons.TKN_MAJOR, tokensAndCons.TKN_MAJEQLS, tokensAndCons.TKN_MINEQLS, tokensAndCons.TKN_PLUS, tokensAndCons.TKN_MINUS, tokensAndCons.TKN_MULT, tokensAndCons.TKN_DIV, tokensAndCons.TKN_PRCTGE, tokensAndCons.TKN_EXCMARK, tokensAndCons.TKN_PAREN_L):
            self.ExprOrVoid()
        #Lvalue
        elif token in (tokensAndCons.TKN_IDENTIFIER):
            self.LValueVoid()
        else:
            self.error+=1
            sys.exit()

    def LValueVoid(self):
        self.LValueVoid_Prime()
        self.LValueExprVoid()

    def LValueVoid_Prime(self):
        token = self.currentToken
        if token in (tokensAndCons.TKN_IDENTIFIER):
            self.next()
        else:
            self.ExprVoid()
            if token in (tokensAndCons.TKN_DOT):
                self.next()
                token = self.currentToken
                if token in (tokensAndCons.TKN_IDENTIFIER):
                    self.next()
            elif token in (tokensAndCons.TKN_SQRBRKT_L):
                self.next()
                self.ExprVoid()
                token = self.currentToken
                if token in (tokensAndCons.TKN_SQRBRKT_R):
                    self.next()
            else:
                self.error+=1
                sys.exit()
    
    def LValueExprVoid(self):
        self.LValueVoid()
        token = self.currentToken
        if token in (tokensAndCons.TKN_EQUALS):
            self.next()
            self.ExprVoid()

    def ExprOrVoid(self):
        self.ExprAndVoid()
        self.ExprOrVoid_Prime()

    def ExprOrVoid_Prime(self):
        token = self.currentToken
        if token in (tokensAndCons.TKN_OR):
            self.next()
            self.ExprAndVoid()
            self.ExprOrVoid_Prime()
        
    def ExprAndVoid(self):
        self.ExprEqualsVoid()
        self.ExprAndVoid_Prime()

    def ExprAndVoid_Prime(self):
        token = self.currentToken
        if token in (tokensAndCons.TKN_AND):
            self.next()
            self.ExprEqualsVoid()
            self.ExprAndVoid_Prime()

    def ExprEqualsVoid(self):   
        self.ExprCompVoid()
        self.ExprEqualsVoid_Prime()

    def ExprEqualsVoid_Prime(self):
        token = self.currentToken
        if token in (tokensAndCons.TKN_DBLEQLS, tokensAndCons.TKN_DISTINCT):
            self.next()
            self.ExprCompVoid()
            self.ExprEqualsVoid_Prime()

    def ExprCompVoid(self):
        self.ExprAddVoid()
        self.ExprCompVoid_Prime()

    def ExprCompVoid_Prime(self):
        token = self.currentToken
        if token in (tokensAndCons.TKN_MAJEQLS, tokensAndCons.TKN_MINEQLS, tokensAndCons.TKN_MINOR, tokensAndCons.TKN_MAJOR):
            self.next()
            self.ExprAddVoid()
            self.ExprCompVoid_Prime()

    def ExprAddVoid(self):
        self.ExprMulVoid()
        self.ExprAddVoid_Prime()

    def ExprAddVoid_Prime(self):
        token = self.currentToken
        if token in (tokensAndCons.TKN_PLUS, tokensAndCons.TKN_MINUS):
            self.next()
            self.ExprMulVoid()
            self.ExprAddVoid_Prime()

    def ExprMulVoid(self):
        self.ExprPreVoid()
        self.ExprMulVoid_Prime()

    def ExprMulVoid_Prime(self):
        token = self.currentToken
        if token in (tokensAndCons.TKN_MULT, tokensAndCons.TKN_DIV, tokensAndCons.TKN_PRCTGE):
            self.next()
            self.ExprPreVoid()
            self.ExprMulVoid_Prime()

    def ExprPreVoid(self):
        self.ExprParenVoid()
        self.ExprPreVoid_Prime()

    def ExprPreVoid_Prime(self):
        token = self.currentToken
        if token in (tokensAndCons.TKN_MINUS, tokensAndCons.TKN_EXCMARK):
            self.next()
            self.ExprParenVoid()
            self.ExprPreVoid_Prime()

    def ExprParenVoid(self):
        token = self.currentToken
        if token in (tokensAndCons.TKN_PAREN_L):
            self.next()
            self.ExprVoid()
            if token in (tokensAndCons.TKN_PAREN_R):
                self.next()

    def FormalsVoid(self):
        self.VariableVoid()
        self.FormalsVoid_Prime()
        

    def FormalsVoid_Prime(self):
        #self.next()
        token = self.currentToken
        if token in (tokensAndCons.TKN_SEMICOLON):
            self.next()
            self.VariableVoid()

    def VariableDeclVoid(self):
        self.VariableVoid()
    
    def VariableVoid(self):
        self.TypeArrayVoid()
        token = self.currentToken
        if token in (tokensAndCons.TKN_SEMICOLON):
            self.next()

    def TypeArrayVoid(self):
        self.TypeVoid()
        # se evalua que despues de el tipo venga un identificador
        token = self.currentToken
        if token in (tokensAndCons.TKN_IDENTIFIER):
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