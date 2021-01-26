from django.shortcuts import render, HttpResponse, redirect

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
<h1>NO-Layout html</h1>
<h2>Sottotitulo | Lista links:</h2>
<ul>
<li><a href="/inizio">Inizio</a></li>
<li><a href="/ciao-mondo">Ciao mondo</a></li>
<li><a href="/pagina-prova">Pagina prova</a></li>
<li><a href="/contatto-pag">Contatto</a></li>
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

    #return HttpResponse(layout + html)
    return render(request, 'inizio.html', {
        'titolo': 'Inizio',
        'variable': 'testo di prova per interpolare variabile.'
    })

def ciao_mondo(request):
    
    # Render sa che deve prendere la vista dentro della cartella templates
    return render(request, 'ciao_mondo.html')

    #return HttpResponse(layout + 
    """
    <h1>Home</h1>
    Ciao mondo con Django!!
    """#)

def pagina(request, reindirizzare=0):

    if reindirizzare == 1:
        return redirect('contatto', nome="Adrian", cognome="Medina") #redirect("/contatto-pag/Adrian/Medina") #redirect('contatto', name="Adrian", cognome="Medina")

    return render(request, 'pagina.html')
    #return HttpResponse(layout + """
    #<h1>Adrian Medina</h1>
    #<h2>Sviluppatore python web django</h2>
    #""")

def contatto(request, nome="", cognome=""): # rendere opzionale con ' ="" '

    html = "<h2>Contatto: </h2>"

    if nome and cognome:
        html += "<p><b>Il nome completo è: </b></p>"
        html += f"""
        <p>{nome} {cognome}</p>
        """
    elif nome or cognome:
        if nome:
            html += f"""<p><b>Il nome è:</b></p>
            <p>{nome}</p>"""
        else:
            html += f"Il cognome è: {cognome}"
    else:
        html += f"<h3>Vuoto</h3>"


    return HttpResponse(layout + html)
