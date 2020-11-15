# CompiladoresURL
Se implementó un escáner léxico basado en el lenguaje mini c#.
## Guía de uso 📋
Al iniciar el ejecutable "Fase1.exe" se abre una consola en la que se solicita la dirección del archivo con el texto a analizar, al terminar el análisis el programa crea un archivo con extensión ".out" en la misma ubicación y con el mismo nombre que el archivo de entrada.
## Implementación
El compilador de mini c# se implementó usando el lenguaje Python, el programa funciona de manera que al leer las lineas del archivo de entrada letra por letra se reconocen distintos tokens por medio de expresiones regulares
### Expresiones regulares utilizadas:
#### ● Para reconocimiento de Palabras Reservadas:
        Reservadas1 = r'^(void|int|double|bool|string|class|const|null|this|for|while|if|else|return|New|Console|Writeline)$'
        Reservadas2 = r'^(interface|foreach|NewArray)$'
#### ● Para reconocimiento de identificadores:
        Identificadores = r'^([a-z]|[A-Z])(([a-z]|[A-Z])|[0-9]|_){0,30}$'
#### ● Para reconocimiento de Enteros:
        Enteros = r'^((0(x|X)([0-9]|[a-f]|[A-F])+)|([0-9]+))$'
        TempHex = r'^0(x|X)$'
#### ● Para reconocimiento de Double:
        Double = r'^(([0-9]+\.[0-9]*(e|E)(\+|-)?[0-9]+)|([0-9]+\.[0-9]*))$'
        TempDouble = r'^[0-9]+\.[0-9]*(e|E)$'
#### ● Para reconocimiento de Parentesis:
        ERParentesis = r'\([^()]*\)'
#### ● Para reconocimiento de Corchetes:
        ERCorchetes = r'\[[^()]*\]'
#### ● Para reconocimiento de Strings:
        StringStep1 =r'^\"[^\"]*$'
        StringStep2 = r'^\"[^\"]*\"$'
#### ● Para reconocimiento de Comentarios:
        OneLineCommentsStep2 = r'^\/\/.*$'
        MultiLineCommentsStep1 = r'^\/\*[^\*\/]*$'
        MultiLineCommentsStep2 = r'^\/\*[^\*\/]*\*$'
        MultiLineCommentsStep3 = r'^\/\*[^\*\/]*\*\/$'
        ExtraCaseComment = r'^\/\*(.)*$'
## Autores
* **José Fernando Oliva Morales 1251518**
* **José Eduardo Meléndez De la Rosa 1059918**


