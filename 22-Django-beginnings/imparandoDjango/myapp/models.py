from django.db import models

# Create your models here.

# Entità/modello articolo, si crea eredando da models.Model
# Dopo si effettueranno le migrazioni e si creerà la tabella omonima 'Article'
# Con la classe meta si configurano i nomi delle tabelle
class Article(models.Model):
    # Definirei campi e tipi di dato.
    # .CharField() Possiede diverse proprietà, esempio quella per definire il numero di caratteri: max_length=100
    # .CharField() Equivale a varchar o text.
    title = models.CharField(max_length=100) 
    content = models.TextField()
    public = models.BooleanField()
    # Salva automaticamente la data solo quando crea il registro la prima volta
    create_at = models.DateTimeField(auto_now_add=True)
    # Salva automaticamente la data esclusivamente di modifica del registro 
    updated_at = models.DateTimeField(auto_now=True) 

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField() # Salva la data manualmente