import fileRW 
import lexer
while True:
    text = input('Ingrese la ruta del archivo a analizar\r\n>')
    result, error = fileRW.read(text)
    if error: 
        print(error)
    else: 
        lexer.Lexer('<stdin>',result)