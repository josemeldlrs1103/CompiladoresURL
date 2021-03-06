#Constantes
CONS_DIGITOS  = '0123456789'
CONS_MAYUS    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CONS_MINUS    = 'abcdefghijklmnopqrstuvwxyz'
#Reservadas
TKN_VOID      = 'T_void'
TKN_INT       = 'T_int'
TKN_DOUBLE    = 'T_double'
TKN_BOOLEAN   = 'T_boolean'
TKN_STRING    = 'T_string'
TKN_CLASS     = 'T_class'
TKN_CONST     = 'T_const'
TKN_INTERFACE = 'T_interface'
TKN_NULL      = 'T_null'
TKN_THIS      = 'T_this'
TKN_FOR       = 'T_for'
TKN_WHILE     = 'T_while'
TKN_FOREACH   = 'T_foreach'
TKN_IF        = 'T_if'
TKN_ELSE      = 'T_else'
TKN_RETURN    = 'T_return'
TKN_BREAK     = 'T_break'
TKN_NEW       = 'T_New'
TKN_NEWARRAY  = 'T_NewArray'
TKN_CONSOLE   = 'T_Console'
TKN_WRITELINE = 'T_WriteLine'
TKN_IDENTIFIER= 'T_identifier'
#Comentarios
TKN_CMT_LINE  = 'T_COMMENT_LINE'
TKN_CMT_OPEN  = 'T_COMMENT_OPEN'
TKN_CMT_CLOSE = 'T_COMMENT_CLOSE'
#Operadores y caracteres
TKN_PLUS      = 'T_PLUS'
TKN_MINUS     = 'T_MINUS'
TKN_MULT      = 'T_MULT'
TKN_DIV       = 'T_DIV'
TKN_PRCTGE    = 'T_PERCENTAGE'
TKN_MINOR     = 'T_MINOR'
TKN_MINEQLS   = 'T_MINOR_EQUALS'
TKN_MAJOR     = 'T_MAJOR'
TKN_MAJEQLS   = 'T_MAJOR_EQUALS'
TKN_EQUALS    = 'T_EQUALS'
TKN_DBLEQLS   = 'T_EQUALS_EQUALS'
TKN_DISTINCT  = 'T_DISTINCT'
TKN_AND       = 'T_AND'
TKN_OR        = 'T_OR'
TKN_EXCMARK   = 'T_EXCLAMATION_MARK'
TKN_SEMICOLON = 'T_SEMICOLON'
TKN_COMMA     = 'T_COMMA'
TKN_DOT       = 'T_DOT'
TKN_PAREN     = 'T_PARENTHESIS'
TKN_PAREN_L   = 'T_LEFT_PARENTHESIS'
TKN_PAREN_R   = 'T_RIGHT_PARENTHESIS'
TKN_SQRBRKT   = 'T_SQUARE_BRACKETS'
TKN_SQRBRKT_L = 'T_LEFT_SQUARE_BRACKET'
TKN_SQRBRKT_R = 'T_RIGHT_SQUARE_BRACKET'
TKN_BRKT      = 'T_BRACKETS'
TKN_BRKT_L    = 'T_LEFT_BRACKETS'
TKN_BRKT_R    = 'T_RIGHT_BRACKETS'

#ExpresionesRegulares
Reservadas1 = r'^(void|int|double|bool|string|class|const|null|this|for|while|if|else|return|New|Console|Writeline)$'
Reservadas2 = r'^(interface|foreach|NewArray)$'
Identificadores = r'^([a-z]|[A-Z])(([a-z]|[A-Z])|[0-9]|_){0,30}$'
Enteros = r'^((0(x|X)([0-9]|[a-f]|[A-F])+)|([0-9]+))$'
TempHex = r'^0(x|X)$'
Double = r'^(([0-9]+\.[0-9]*(e|E)(\+|-)?[0-9]+)|([0-9]+\.[0-9]*))$'
TempDouble = r'^[0-9]+\.[0-9]*(e|E)$'
ERParentesis = r'\([^()]*\)'
ERCorchetes = r'\[[^()]*\]'
StringStep1 =r'^\"[^\"]*$'
StringStep2 = r'^\"[^\"]*\"$'
OneLineCommentsStep1 = r'^\/$'
OneLineCommentsStep2 = r'^\/\/.*$'
MultiLineCommentsStep1 = r'^\/\*[^\*\/]*$'
MultiLineCommentsStep2 = r'^\/\*[^\*\/]*\*$'
MultiLineCommentsStep3 = r'^\/\*[^\*\/]*\*\/$'
ExtraCaseComment = r'^\/\*(.)*$'