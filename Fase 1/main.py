import fileRW
while True:
    text = input('Ingrese la ruta del archivo a analizar\r\n>')
    result, error = fileRW.read(text)

    if error: 
        print(error.as_string())
    else: 
        print(result)