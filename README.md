# CompiladoresURL.
Se implementó un escáner semántico basado en c# basado en el lenguaje mini c#.
## Descripción tabla de símbolos📖
para la tabla de símbolos se implemento un tipo de dato abtracto en el que se almacena el nombre, tipo de dato y valor de las variables declaradas, así como el número de línea y rango de columnas en las que se encuentra escrita dentro del archivo, y agregando cada uno a una lista "Tabla de símbolos".
El valor de las variables se calcula utilizando los elementos de la lista que se encuentra en la misma linea, se utiliza el símbolo como indicador de la variable en la que se debe almacenar el valor una vez se han realizado todas las operaciones en la línea, considerando y respetando la compatibilidad entre los tipos de dato.
## Manejo de errores  ⚠️
Si durante el proceso de cálculo del valor se encuentra que los valores de las variables a operar no son compatibles se reporta dentro del historial que se lleva de las variables de la tabla de símbolos.
## Consideraciones Generales 🛑
Para la ejecucción correcta los archivos "LRTable.txt" y "ProductionRules.txt" deben estar en la misma carpeta que el ejecutable
## Librería para apoyo visual 👀
Al imprimir la tabla del historial de la tabla de símbolos y la tabla de símbolos se utilizó una librería externa que ayuda con la impresión en forma de tabla en su representación ascii    **Link al sitio de la librería utilizada** [Pretty table](https://pypi.org/project/prettytable/)
## Autores ✒️
* **José Fernando Oliva Morales 1251518** [feroliv4z](https://github.com/feroliv4z)
* **José Eduardo Meléndez De la Rosa 1059918** [josemel1103](https://github.com/josemeldlrs1103)

