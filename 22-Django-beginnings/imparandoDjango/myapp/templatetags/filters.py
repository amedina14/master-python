"""
Per creare filtri personalizzati si deve
- importare il modulo template di django
- caricare la libreria di template
"""
from django import template

register = template.Library()

# Decorator: funzionalità previa che gli si da ad una classe o funzione.
@register.filter(name='saluto')
def saluto(value):

    msg = ""
    if len(value) >= 9:
        msg += "<p>Il tuo nome è troppo lungo, supera gli 8 caratteri<p>"

    return f"<h1 style='background-color:#2BA977;color=white;'>Benvenuto, {value}</h1>"+msg

# Perchè i filtri funzionino, la cartella che li contiene 'templatetags' 
# deve avere la sotto cartella __pycache__ che si crea in automatico e contiene: 
# __init__.cpython-38.pyc e filters.cpython-38.pyc 
# Lo stesso vale per: 
# 22-Django-beginnings\imparandoDjango\imparandoDjango\__pycache__ 
# 22-Django-beginnings\imparandoDjango\myapp\__pycache__