class Mago:
    def hechizos(self):
        print("El DarkLord lanza un poderoso hechizo")

class Guerrero(Mago):
    def defensa(self):
        print("El DarkLord usa su defensa legendaria")

class Elfo(Mago):
    def aura(self):
        print("El DarkLord libera un aura mágica")

class DarkLord(Guerrero, Elfo):
    pass

d = DarkLord()

print(" Herencia con guerrero y elfo ")
d.hechizos()
d.defensa()
d.aura()

print("\nMRO:")
print(DarkLord.mro())

class DarkLord2(Elfo, Guerrero):
    pass

d2 = DarkLord2()

print("\n Herencia con elfo y guerrero ")
d2.hechizos()
d2.defensa()
d2.aura()

print("\nNuevo MRO:")
print(DarkLord2.mro())