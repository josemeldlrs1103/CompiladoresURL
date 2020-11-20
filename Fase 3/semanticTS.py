import stateNode
import tokensAndCons
class semanticTS:
     def __init__(self,tokensList):
        TS = []
        previous = None
        permite = ['int','double','bool','string','const']
        ##se añaden todos los tokens a la la TS
        for element in tokensList:
            if(previous is not None and previous.Name in permite):
                # se verifica que el token sea apto para añadirlo a la TS
                if (element.Token in tokensAndCons.AbleToTS and element.Name not in tokensAndCons.excludedName):
                    TS.append(stateNode.elementTS(element.Token, previous.Name ,element.Name, element.Value, element.Line,element.Column))
                    if(element.Token == tokensAndCons.TKN_IDENTIFIER):
                        permite.append(str(element.Name))
            previous = element
        print('debug')