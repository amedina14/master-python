# Liste con dizionari
print("\n### Liste con dizionari ###")
contatti = [
    {
        "nome": "Adrian",
        "email": "adrian@mail.com"
    },
    {
        "nome": "Sofia",
        "email": "sofia@mail.com"
    },
    {
        "nome": "victor",
        "email": "victor@mail.com"
    }
]

print(contatti)
"""
### Liste con dizionari ###
[{'nome': 'Adrian', 'email': 'adrian@mail.com'}, {'nome': 'Sofia', 'email': 'sofia@mail.com'}, {'nome': 'victor', 'email': 'victor@mail.com'}]
"""



print("\n## Nome primo elemento ##")
contatti[0]["nome"] = "Adriano"
print(contatti[0]["nome"])
"""
## Nome primo elemento ##
Adriano
"""



print("\n## Nomi ##")
for contatto in contatti:
    print(contatto["nome"])
print("\n## Emails ##")
for contatto in contatti:
    print(contatto["email"])
"""
## Nomi ##
Adriano
Sofia
victor

## Emails ##
adrian@mail.com
sofia@mail.com
victor@mail.com
"""



print("\n## Tabella Valori ##")
for contatto in contatti:
    for chiave in contatto:
        print(f"{contatto[chiave]}\t", end="| ")
    print()
"""
## Tabella Valori ##
Adriano | adrian@mail.com       |
Sofia   | sofia@mail.com        |
victor  | victor@mail.com       |
"""



print("\n## Tabella completa: chiave > valore ##")
for contatto in contatti:
    for chiave in contatto:
        print(f"{chiave}:\t{contatto[chiave]}\t", end="| ")
    print()
"""
## Tabella completa: chiave > valore ##
nome:   Adriano | email:        adrian@mail.com |
nome:   Sofia   | email:        sofia@mail.com  |
nome:   victor  | email:        victor@mail.com |
"""



print("\n## Gruppi di contatti ##")
for contatto in contatti:
    print(contatto["nome"])
    print(contatto["email"])
    print("----------------")
"""
## Gruppi di contatti ##
Adriano
adrian@mail.com
----------------
Sofia
sofia@mail.com
----------------
victor
victor@mail.com
----------------
"""
