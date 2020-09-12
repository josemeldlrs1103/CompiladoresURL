# CompiladoresURL
Se implementó un escáner léxico basado en el lenguaje mini c#.
## Guía de uso 📋
Al iniciar el ejecutable se abre una consola en la que se solicita la dirección del archivo con el texto a analizar, al terminar el análisis el programa crea un archivo con extensión ".out" en la misma ubicación y con el mismo nombre que el archivo de entrada.
## Gramática corregida
Program				::= Decl Program'
Program'			::= Program | ε
Decl 	    		::= Decl' Decl
Decl'		    	::= VariableDecl | FunctionDecl
VariableDecl 		::= Variable ;
Variable 	    	::= TypeA ident
TypeA				::= Type Array
Array				::= [] | ε 
Type 	    		::= int | double | bool | string | ident 
FunctionDecl 		::= FunctionDecl' ident (Formals) Stmt
FunctionDecl'		::= Type | void
Formals	        	::= Variable Formals' | ε 
Formals'			::=	,Variable | ε
Stmt 		    	::= IfStmt | WhileStmt | Expr ; | ε 
IfStmt 	       		::= if (Expr) Stmt IfStmt'
IfStmt'	       		::= else Stmt | ε
WhileStmt   		::= while (Expr) Stmt
Expr 	        	::= Constant | this | New(ident) | ExprOr | LValue
ExprOr				::= ExprAnd ExprOr'
EsprOr' 			::= || ExprAnd ExprOr' | ε
ExprAnd				::= ExprEquals ExprAnd'
EsprAnd' 			::= && ExprEquals ExprAnd' | ε
ExprEquals			::= ExprComp ExprEquals'
ExprEquals'			::= == ExprComp ExprEquals' | != ExprComp ExprEquals' | ε
ExprComp			::= ExprAdd ExprComp'
ExprComp'			::= < ExprAdd ExprComp' | > ExprAdd ExprComp' | <= ExprAdd ExprComp' | >= ExprAdd ExprComp' | ε
ExprAdd				::= ExprMul ExprAdd'
ExprAdd'			::= + ExprMul ExprAdd' | - ExprMul ExprAdd' | ε
ExprMul				::= ExprPre ExprMul'
ExprMul'	        ::= * ExprPre ExprMul' | / ExprMul ExprAdd' | % ExprMul ExprAdd' | ε 
ExprPre				::= ExprParen ExprPre'
ExprPre'			::= - ExprParen ExprPre' | ! ExprParen ExprPre' | ε
ExprParen			::= (Expr) | ε
LValue	    		::= LValue' LValueExpr
LValue'             ::= ident | Expr.ident | Expr [Expr] | ε
LValueExpr          ::= LValue = Expr | ε
Constant	    	::= intConstant | doubleConstant | boolConstant | stringConstant | null
## Manejo de errores 
Al encontrar un error el parser salta hacia la siguiente línea, regresando hasta la producción inicial de la gramática, se valida que al momento de retomar el parseo la producción lleve hacia la declaración de una variable o una función, en caso de no encontrar ninguna de las producciones el analisis termina.
## Autores
* **José Fernando Oliva Morales 1251518**
* **José Eduardo Meléndez De la Rosa 1059918**