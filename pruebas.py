
print("\n--------------LISTA-INICIAL-CON-CARACTERES-ESPECIALES--------------")
lista = ["Social humanistica", "12\n", "017", "017", "Compiladores", "017"]
print("Lista actual: " + str(lista))

print("\n-------------------LISTA-EN-FORMA-DE-STRING------------------------")
nueva_en_string = str(list(map(str.strip, lista)))
print("Lista nueva: " + nueva_en_string)

print("\n------------CONVERSION---STRING-A-LISTA----------------------------")
lista_nueva = eval(nueva_en_string)
print(lista_nueva)

print("Esta es la cantidad de veces que repite 017: ", lista_nueva.count("017"))
print("Esta es la posicion del primer elemento 017 que hay en lista: ", lista_nueva.index("017"))
