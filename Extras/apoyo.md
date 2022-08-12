# MODOS DE ACCESO

solo lectura {r} #abre el archivo unicamente para leerlo

solo escritura {w} #abre el archivo unicamente para escribir en el

lectura y escritura {r+} #abre el archivo para lectura y escritura. el archivo tiene que existir

escritura y lectura {w+} #sobreescribe la data existente en el archivo

adjuntar {a} #abre el archivo apra escritura. los datos sone scritos al final del archivo

solo escritura {a+} #abre el archivo para lectura y escritura. los datos escritos al final del archivo

# ABRIR UN ARCHIVO
objeto = open("nombre.extension", "modo de acceos")

# CERRAR UN ARCHIVO
objeto.close()

# ESCRIBIR EN UN ARCHIVO
objeto = open("ejemplo.txt", "rt")
objeto.write("hola mundo")
objeto.close()

# LEER DATOS DE UN ARCHIVO
objeto.read()
objeto.readLine()
objeto.readLines()

