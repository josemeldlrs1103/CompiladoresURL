import fileRW 
import lexer
import parserCls
while True:
    Text = input('Ingrese la ruta del archivo a analizar\r\n>')
    Result, error = fileRW.read(Text)
    if error: 
        print(error)
    else:
        Element = ''
        Lines = lexer.Lexer(Result)
        SymbolTab, TokensTab = Lines.EvaluateLines()
        ErrorQuantity = lexer.ErrorQuantity
        if(ErrorQuantity != 0):
            Element ='El archivo cuenta con: ' + str(ErrorQuantity) + ' errores.'
        else:
            Element = 'El archivo no cuenta con errores.'
        #for Element in SymbolTab:
            print (Element)
        #fileRW.write(Text, SymbolTab)
    if (len(TokensTab) > 0):
        try:
            p1 = parserCls.ParserCls(TokensTab)
            p2 = p1.ProgramVoid()
            print(p2)
        except:
            print ('')
    else:
        print ('El archivo analizado solamente tiene comentarios')
