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

layout = """
<h1>Layout html</h1>
<h2>Sottotitulo | Lista links:</h2>
<ul>
<li><a href="/inizio">Inizio</a></li>
<li><a href="/ciao-mondo">Ciao mondo</a></li>
<li><a href="/pagina-prova">Pagina prova</a></li>
</ul>
<hr/>
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

    html += "<br/><hr/>"
    n = 1000
    for n in range(1000,1051):
        if n%2 == 0:
            html += f"<li>{str(n)}</li>"

    html += "</ul>"

    return HttpResponse(layout + html)

def ciao_mondo(request):
    return HttpResponse(layout + """
    <h1>Home</h1>
    Ciao mondo con Django!!
    """)

def pagina(request):
    return HttpResponse(layout + """
    <h1>Adrian Medina</h1>
    <h2>Sviluppatore python web django</h2>
    """)
