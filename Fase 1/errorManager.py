def incomplete (line, stringFound):
    result = "*** Error encontrado en la línea: "+str(line) + " se encontro el valor incompleto nos válido: "+str(stringFound) +" ***"
    return result

def notValid (line, stringFound):
    result = "*** Error encontrado en la línea: "+str(line) + " se encontro el caracter nos válido: "+str(stringFound) +" ***"
    return result

def expected (line, col, open, close):
    result = "**Error encontrado en la línea: "+str(line)+" el par no esta completo, se estperaba: "+str(open)+" o "+str(close)+"***"
    return result
