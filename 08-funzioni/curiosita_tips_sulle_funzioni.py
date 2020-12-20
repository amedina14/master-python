#tip 1
"""
E' preferibile definire le funzioni nella parte di sopra del codice 
"""

def bad_function():
    print("Bad practices")

bad_function()

#tip 2
"""
E' preferibile che una funzione sempre restituisca un dato "return"
"""
def good_function():
    return "Good practices"
text = good_function()
print(text)

#tip 3
"""
Si possono chiamare variabili globali dalle funzioni, ma quest'ultime
devono essere invocate dopo tali variabili globali.
"""
def saluta():
    return "Ciao "+nome

nome = "Adrian" #Variabile globale
print(saluta())

#tip 4
"""
Buona pratica è passare i dati come parametri alle funzioni
"""
def auguri(festa):
    return "Auguri "+festa

natale = "di buon Natale"
print(auguri(natale))
