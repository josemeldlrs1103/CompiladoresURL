import fileRW 
import lexer
import ascentParser
import semanticTS
while True:
    Text = input('Ingrese la ruta del archivo a analizar\r\n>')
    Result, error = fileRW.read(Text)
    if error: 
        print(error)
    else:
        Lines = lexer.Lexer(Result)
        SymbolTab, TokensTab = Lines.EvaluateLines()
        ErrorQuantity = lexer.ErrorQuantity
        if(ErrorQuantity != 0):
            print('El archivo cuenta con: ' + str(ErrorQuantity) + ' errores lexicos.')
        else:
            print('El archivo no cuenta con errores lexicos.')
            ascentParser.ascentParser(TokensTab)
            semanticTS.semanticTS(TokensTab)
