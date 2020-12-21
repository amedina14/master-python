# Liste multidimensionali
print("\n#### Lista multidimensionale ####")
contatti = [
    [
        "Adrian",
        "adrian@mail.com"
    ],
    [
        "Sofia",
        "sofia@mail.com"
    ],
    [
        "Victor",
        "victor@mail.com"
    ]
]
print(contatti)
print()

for unContatto in contatti:
    for ogni_dato in unContatto:
        print(f"{ogni_dato}\t", end="| ")
    print()

"""
#### Lista multidimensionale ####
[['Adrian', 'adrian@mail.com'], ['Sofia', 'sofia@mail.com'], ['Victor', 'victor@mail.com']]

Adrian  | adrian@mail.com       |
Sofia   | sofia@mail.com        |
Victor  | victor@mail.com       |

"""

print("\n## Lista di email ##")
for contatto in contatti:
    print("mail: \t"+contatto[1])

"""
mail:   adrian@mail.com
mail:   sofia@mail.com
mail:   victor@mail.com
"""

print("\n## Gruppi di dati ##")
for contatto in contatti:
    for dato in contatto:
        if contatto.index(dato) == 0:
            print(f"nome: {dato}")
        else:
            print(f"email: {dato}")
    print()