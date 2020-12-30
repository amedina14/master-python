import classi

persona = classi.Persona()

persona.setNome("Adrian")
persona.setCognome("Medina")
persona.setAltezza("1.64")
persona.setEta("24")

print(f"La persona è: {persona.getNome()} {persona.getCognome()} {persona.getAltezza()} {persona.getEta()}")
print(persona.parlare())
print(persona.dormire())
