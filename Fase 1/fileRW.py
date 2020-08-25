import os
def read(text):
    Extention = list(text)
    Error = None
    Tokens = None
    if(len(Extention)>0):
        if((Extention[len(Extention)-4]=='f' and Extention[len(Extention)-3]=='r' and Extention[len(Extention)-2]=='a' and Extention[len(Extention)-1]=='g')or(Extention[len(Extention)-3]=='t' and Extention[len(Extention)-2]=='x' and Extention[len(Extention)-1]=='t')):
            File1= open(text,'r')
            Tokens= File1.readlines()
            if((len(Tokens))==0):
                Error='El archivo está vacío'
        else:
            Error = 'La extensión del archivo no es compatible'
    else:
        Error = 'Por favor ingrese una dirección'
    return Tokens, Error


def write(Text, SymbolTab):
    fileName = os.path.splitext(os.path.basename(Text))[0]
    fileRoute = os.path.splitext(os.path.dirname(Text))[0]
    file = open(fileRoute + "\\"+ fileName + ".out", "w")
    for Element in SymbolTab:
        file.write(Element+"\n")
    file.close()
