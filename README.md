# CompiladoresURL
Se implementó un escáner semántico basado en c# basado en el lenguaje mini c#.
## Gramática implementada 📖
La gramática modificada se encuentra en la carpeta, si desea verla ahora haga click en el siguiente enlace 
* **Enlace a gramática** [ProductionRules.txt](https://github.com/josemeldlrs1103/CompiladoresURL/blob/fase2/Fase%202/ProductionRules.txt)
## Tabla de análisis  📝
el analizador semántico se implementó en base al método SLR, la tabla de análisis es la siguiente:
* **Enlace a tabla de análisis** [SLRTables.xlsx]()
## Manejo de errores  ⚠️
Cuando el analizador encuentra un error se ignora el token inesperado, y se reporta que dicho token no se espera en esa posición de la cadena, una vez omitido el analizador continúa con el proceso de análisis, si al consumir todos los tokens de la cadena el analizador llega al estado de aceptación se indica que la cadena es válida, en caso contrario la cadena se rechaza completamente.
## Autores ✒️
* **José Fernando Oliva Morales 1251518** [feroliv4z](https://github.com/feroliv4z)
* **José Eduardo Meléndez De la Rosa 1059918** [josemel1103](https://github.com/josemeldlrs1103)
