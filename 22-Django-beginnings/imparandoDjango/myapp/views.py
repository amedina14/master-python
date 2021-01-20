from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modello Vista Controller => Azioni (metodi) 
# MVT = Modello Template Vista => Azioni (metodi)

"""
Bisogna passargli come parametro 'request' a tutti i metodi del template di django,
importato da HttpResponse.
Il request è un parametro che permette di ricevere dati di richieste http all'url.


Per visualizzare i risultati dei metodi, bisogna stabilirgli le url: urls.py

"""

def inizio(request):

    html = """
    <h1>Inizio</h1>
    <p>Anni fino al 2050:</p>
    <ul>
    """
    year = 2021

    #for i in range(year,2051):
    while year <= 2051:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"

    return HttpResponse(html)

def ciao_mondo(request):
    return HttpResponse("""
    <h1>Home</h1>
    Ciao mondo con Django!!
    """)

def pagina(request):
    return HttpResponse("""
    <h1>Adrian Medina</h1>
    <h2>Sviluppatore python web django</h2>
    """)
