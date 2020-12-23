"""
Esercizio 4
4 variabili
-normale
-funzionale (con funzioni)
"""
var1 = []
var2 = "stringa"
var3 = 3
var4 = True

lista_var = [var1, var2, var3, var4]

print(f"\n{type(var1)}, {type(var2)}, {type(var3)}, {type(var4)}\n")

def stampaTipo(tipo):
        if tipo == list:
            result = "list".upper()
        elif tipo == str:
            result = "str".upper()
        elif tipo == int:
            result = "int".upper()
        elif tipo == bool:
            result = "bool".upper()
        return result

def verificaTipo(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""

    if test:
        result += f"\"{dato}\" E' di tipo {stampaTipo(tipo)}"
    else:
        result = None

    return result

"""
    for dato in lista_var:
        if type(dato) == list:
            print(f"{lista_var.index(dato)}. \"{dato}\" E' di tipo list")
        elif type(dato) == str:
            print(f"{lista_var.index(dato)}. \"{dato}\" E' di tipo str")
        elif type(dato) == int:
            print(f"{lista_var.index(dato)}. \"{dato}\" E' di tipo int")
        elif type(dato) == bool:
            print(f"{lista_var.index(dato)}. \"{dato}\" E' di tipo bool")
"""

print(verificaTipo(var1,list))
print(verificaTipo(var2,str))
print(verificaTipo(var3,int))
print(verificaTipo(var4,bool))


"""
dato = input("Inserisci dato: ")
tipo = input("Inserisci tipo: ")
print(verificaTipo(dato, tipo))
"""