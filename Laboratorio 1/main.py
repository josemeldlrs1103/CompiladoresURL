import fileRW 
import lexer
import parserCls
import newSecuence
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
            SymbolTab.append('El archivo cuenta con: ' + str(ErrorQuantity) + ' errores.')
        else:
            SymbolTab.append('El archivo no cuenta con errores.')
        for Element in SymbolTab:
            print (Element)
        fileRW.write(Text, SymbolTab)
    ## esto de abajo es para probar el funcionamineto del paso de parametros, borrar luego
    if (len(TokensTab) > 0):
        p1 = parserCls.ParserCls(TokensTab)
        p1.ProgramVoid()
    else:
        print ('El archivo analizado solamente tiene comentarios')
