from classi import classi

# Persona normale
persona = classi.Persona()

persona.setNome("Adrian")
persona.setCognome("Medina")
persona.setAltezza("1.64")
persona.setEta("24")

print(f"La persona è: {persona.getNome()} {persona.getCognome()} {persona.getAltezza()} {persona.getEta()}")
print(persona.parlare())
print(persona.dormire())

# Persona informatico
informatico = classi.Informatico()
if type(informatico) == classi.Informatico:
    print("-------Informatico------")
    informatico.setNome("Adrian")
    informatico.setCognome("Medina")
    print(f"L'informatico è: {informatico.getNome()} {informatico.getCognome()}")
    print(f"Impara: {informatico.imparare('Php')}")
    print(f"Azione: {informatico.programmare()}")
    print(informatico.getLinguaggi())

# Tecnico di reti
tecnico = classi.TecnicoReti()
if type(tecnico) == classi.TecnicoReti:
    print("-------Tecnico Reti-------")
    tecnico.setLinguaggi("")
    tecnico.imparare("Assembly")
    print(f"Livello: {tecnico.auditReti} | Linguaggi: {tecnico.getLinguaggi()}")
    print(tecnico.audit())