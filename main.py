class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(f"--- {self.nombre} ---")
        print(f"· Fuerza: {self.fuerza}")
        print(f"· Inteligencia: {self.inteligencia}")
        print(f"· Defensa: {self.defensa}")
        print(f"· Vida: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"☠️ {self.nombre} ha muerto.")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño_provocado = self.daño(enemigo)
        if daño_provocado < 0:
            daño_provocado = 0
            
        enemigo.vida -= daño_provocado
        print(f"⚔️ {self.nombre} ha hecho {daño_provocado} puntos de daño a {enemigo.nombre}.")
        
        if enemigo.esta_vivo():
            print(f"La vida actual de {enemigo.nombre} es {enemigo.vida}.")
        else:
            enemigo.morir()


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def atributos(self):
        super().atributos()
        print(f"· Espada (Bono): {self.espada}")

    def daño(self, enemigo):
        return (self.fuerza * self.espada) - enemigo.defensa


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print(f"· Libro (Bono): {self.libro}")

    def daño(self, enemigo):
        return (self.inteligencia * self.libro) - enemigo.defensa


def iniciar_combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\n=== TORNEO - TURNO {turno} ===")
        jugador_1.atacar(jugador_2)
        if not jugador_2.esta_vivo():
            break
            
        jugador_2.atacar(jugador_1)
        turno += 1

    print("\n=============================")
    print("      FIN DEL COMBATE        ")
    print("=============================")
    if jugador_1.esta_vivo():
        print(f"🏆 ¡{jugador_1.nombre} ha ganado el combate!")
    else:
        print(f"🏆 ¡{jugador_2.nombre} ha ganado el combate!")


if __name__ == "__main__":
    Johan = Guerrero("Johan", 20, 10, 5, 100, 5)
    Nicolas = Mago("Nicolas", 10, 15, 10, 100, 5)

    print("ESTADÍSTICAS INICIALES:")
    Nicolas.atributos()
    Johan.atributos()

    iniciar_combate(Nicolas, Johan)