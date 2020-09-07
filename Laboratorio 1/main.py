import fileRW 
import lexer

while True:
    Text = input('Ingrese la ruta del archivo a analizar\r\n>')
    Result, error = fileRW.read(Text)
    if error: 
        print(error)
    else:
        Lines = lexer.Lexer(Result)
        SymbolTab= Lines.EvaluateLines()
        ErrorQuantity = lexer.ErrorQuantity
        if(ErrorQuantity != 0):
            SymbolTab.append('El archivo cuenta con: ' + str(ErrorQuantity) + ' errores.')
        else:
            SymbolTab.append('El archivo no cuenta con errores.')
        for Element in SymbolTab:
            print (Element)
        fileRW.write(Text, SymbolTab)
