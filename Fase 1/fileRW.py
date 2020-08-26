import os
def read(text):
    Extention = list(text)
    Error = None
    Tokens = None
    try:
        if(len(Extention)>0):
            File1= open(text,'r')
            Tokens= File1.readlines()
            if((len(Tokens))==0):
                Error='El archivo está vacío'
        else:
            Error = 'Por favor ingrese una dirección'
    except:
        Error = 'El ruta o el archivo ingresado no existe'
    return Tokens, Error


def write(Text, SymbolTab):
    file = open(os.path.splitext(Text)[0] + ".out", "w")
    for Element in SymbolTab:
        file.write(Element+"\n")
    file.close()
