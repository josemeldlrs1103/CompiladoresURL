def incomplete (line, stringFound):
    result = "*** Error encontrado en la línea: "+str(line) + " se encontro el valor incompleto no es válido: "+str(stringFound) +" ***"
    return result

def notValid (line, stringFound):
    result = "*** Error encontrado en la línea: "+str(line) + " se encontro el caracter no es válido: "+str(stringFound) +" ***"
    return result

def expected (line, col, open, close):
    result = "**Error encontrado en la línea: "+str(line)+" el par no esta completo, se estperaba: "+str(open)+" o "+str(close)+"***"
    return result

def parserNotExpected (line, col, token):
    result = 'Error en la linea ' + line + ' , ' + col +' Token no esperado: ' + token
    return result