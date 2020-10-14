import fileRW 
import lexer
while True:
    Text = input('Ingrese la ruta del archivo a analizar\r\n>')
    Result, error = fileRW.read(Text)
    if error: 
        print(error)
    else:
        Lines = lexer.Lexer(Result)
        SymbolTab, TokensTab = Lines.EvaluateLines()
        ErrorQuantity = lexer.ErrorQuantity
        

        for Element in SymbolTab:
            print (Element)
        #fileRW.write(Text, SymbolTab)
        if(ErrorQuantity != 0):
            print('El archivo cuenta con: ' + str(ErrorQuantity) + ' errores.')
        else:
            print('El archivo no cuenta con errores.')