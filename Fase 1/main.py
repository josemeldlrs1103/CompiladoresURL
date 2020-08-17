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
        for Element in SymbolTab:
            print (Element)