from curso_model import Curso
from gestionar_curso import DB

class CargarArchivo:
    lista = []
    sulist = []

    with open("entrada.LFP", "r") as archivo:
        lines = archivo.readlines()
        print(lines)
        #for linea in archivo:
            #lista.append(linea.rstrip())
            #print(linea)

    print("-------------------")
    for line in lines:
        print(line.rstrip())

        lista.append(line.split(","))
        
    print(".......................")
    #print("letra dentro de la lista")
    #separacion = lista[3][4]
    #print(separacion)
    print(lista)
    print(".......................")
    print(lista[0][0])#codigo
    codigo =lista[0][0]
    print(lista[0][1])#nombre
    nombre = lista[0][1]
    print(lista[0][2])#prerequisito
    prerequisito = lista[0][2]
    print(lista[0][3])#obligatorio
    obligatorio = lista[0][3]
    print(lista[0][4])#semestre
    semestre = lista[0][4]
    print(lista[0][5])#creditos
    creditos = lista[0][5]
    print(lista[0][6])#estado
    estado = lista[0][6]

    objeto = Curso(codigo, nombre, prerequisito, obligatorio, semestre,
    creditos, estado)
    DB.imprimir_nombre(objeto)

    #print("imprimir linea entera en una lista")
    #print(lista[3].split(","))
