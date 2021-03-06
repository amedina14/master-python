from django.shortcuts import render, HttpResponse, redirect
from myapp.models import Article, Category

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

    # Esempio con il metodo HttpResponse
    """
    html = ""
    <h1>Inizio</h1>
    <p>Anni fino al 2050:</p>
    <ul>
    ""
    year = 2021

    #for i in range(year,2051):
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "<br/><hr/>"
    n = 1000
    for n in range(1000,1051):
        if n%2 == 0:
            html += f"<li>{str(n)}</li>"

    html += "</ul>"
    """

    # Esempi con template language of django
    nome="Adrian Medina"
    languages = ["javascript","java",".net","python","php"]
    #languages = []

    year = 2021
    rango = range(year,2051)

    #return HttpResponse(layout + html)
    return render(request, 'inizio.html', {
        'titolo': 'Inizio',
        'variable': 'testo di prova per interpolare variabile.',
        'nome': nome,
        'languages': languages,
        #'year': year,
        'rango': rango,
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

    return render(request, 'pagina.html', {
        'testo': 'Fare la spesa',
        'priorita': ['Bassa','Media','Alta'],
        'frasi': ["“Misurare i progressi della programmazione dalle linee di codice è come misurare i progressi nella costruzione di aerei dal loro peso.” Bill Gates",
        "“I bravi programmatori sanno cosa scrivere. I migliori sanno cosa riscrivere.” ERIC STEVEN RAYMOND",
        "“Distribuisci presto. Distribuisci spesso. E presta ascolto agli utenti.” ERIC STEVEN RAYMOND",
        "“Un sistema di sicurezza è sicuro soltanto finché è segreto.” ERIC STEVEN RAYMOND",
        "“Einstein ha argomentato che ci devono essere spiegazioni semplificate della natura, perché Dio non è capriccioso o arbitrario. Tale fede non è di conforto al programmatore di software.” FREDERICK PHILLIPS BROOKS JR.",
        "“Un pessimo programmatore può creare due posti di lavoro all'anno. ” DAVE PARNAS",
        "“L'istruzione alla scienza del computer non può rendere chiunque un programmatore esperto più di quanto lo studio dei pennelli e dei colori possa rendere qualcuno un pittore esperto.” ERIC STEVEN RAYMOND",
        "“Nelle conversazioni personali con personale tecnico, io mi definisco un hacker. Ma quando sto parlando coi giornalisti dico solo ‘programmatore’ o qualcosa di simile.” CISCO HOUSTON",
        "“Programmare è un atto innaturale.” ALAN PERLIS",
        "“Riposa in pace, Steve Jobs. Scommetto che in questo momento sei occupato a rivoluzionare l'Aldilà per rendere il nostro arrivo migliore.” JOE SATRIANI",
        "“1. Se la modifica di un programmatore a un programma esistente funziona, probabilmente non era quello che voleva il cliente. 2. Il cliente non sa quello che vuole, ma sa quello che non vuole.” ARTHUR BLOCH",
        "“I vecchi programmatori non muoiono mai: rinunciano solo alle loro risorse.”",
        "“Non è necessario essere pazzi per essere un webmaster (ma aiuta).”",
        "“Non c'è linguaggio in cui sia difficile scrivere cattivi programmi.” ARTHUR BLOCH"]
    })
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

def create_article(request, title, content, public):
    article = Article(
        title = title,
        content= content,
        public= public,
    )
    # Persistenza nel DB
    article.save()

    return HttpResponse(f"Article created: <b>{article.title}</b> - {article.content}")

def legge_articolo(request, id):

    # Facciamo uso del modello per leggere i valori del DB
    # Accede al modello > ai suoi oggetti > e prendi un solo registro (get)
    try:
        articolo = Article.objects.get(id=id, public=True)
        errore = "Articolo caricato con successo"
        #response = f"Articolo: <b>{articolo.title}</b>"
    except:
        errore = f"<b>Articolo non trovato</b>"

    #return HttpResponse(response)
    return render(request,'leggi_articolo.html', {
        'articolo': articolo,
        'errore': errore,
    })

def modifica_articolo(request, id):

#    try:
    articolo = Article.objects.get(pk=id)
    articolo.title = "Framework Django per Python"
    articolo.content = "Orientato allo sviluppo web, è molto veloce creare contenuti con Django"
    articolo.public = True
    articolo.save()
    response = f"Articolo modificato: <p><b>{articolo.title}</b></p><p>{articolo.content}</p><p>{articolo.public}</p>"
#    except:
#        response = f"<b>Articolo non trovato</b>"
    
    return HttpResponse(response)

def elenco_articoli(request):
    
    #articoli = Article.objects.all()
    # Ordina discendentemente: dalla modifica del articolo più recente alla più vecchia.
    # Limita il numero di righe da visualizzare [3:7]
    articoli = Article.objects.order_by('-updated_at')[0:10]
    #preview = Article.objects.all('content')[:200]


    return render(request, 'articoli.html', {
        'articoli': articoli,
        #'preview': preview,
    })

def elimina_articolo(request, id):

    articolo = Article.objects.get(pk=id)
    articolo.delete()

    return redirect('elenco')