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

def readLRTable():
    Error = None
    Table = None
    Status = []
    path1 = os.path.join(os.path.abspath(os.path.dirname(__file__)),'LRTable.txt')
    try:
        File1 = open('LRTable.txt','r')
        Table = File1.readlines()
        if((len(Table))==0):
            Error='El archivo con la tabla LR está vacío'
        for Element in Table:
            Status.append(Element[:-1])
    except:
        Error = 'El archivo con la tabla LR no existe'
    return Status, Error

def readProductionRules():
    Error = None
    Table = None
    Status = []
    path2 = os.path.join(os.path.abspath(os.path.dirname(__file__)),'ProductionRules.txt')
    try:
        File1 = open('ProductionRules.txt','r')
        Table = File1.readlines()
        if((len(Table))==0):
            Error='El archivo con las reglas de la gramática está vacío'
        for Element in Table:
            Status.append(Element[:-1])
    except:
        Error = 'El archivo con las reglas de la gramática no existe'
    return Status, Error