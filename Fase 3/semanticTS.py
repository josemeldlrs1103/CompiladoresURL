import stateNode
import tokensAndCons
class semanticTS:
     def __init__(self,tokensList):
        TS = []
        ##se añaden todos los tokens a la la TS
        for element in tokensList:
            # se verifica que el token sea apto para añadirlo a la TS
            if (element.Token in tokensAndCons.AbleToTS and element.Name not in tokensAndCons.excludedName):
                TS.append(stateNode.elementTS(element.Token, element.Name, element.Value, element.Line,element.Column))
 