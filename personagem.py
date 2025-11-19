class Personagem:
    def __init__(self, nome, forca, defesa, vida=100, xp=0):
        self.nome = nome
        self.forca = forca
        self.defesa = defesa
        self.vida = vida
        self.xp = xp

    def mostrar_status(self):
        print(f"\nStatus do Personagem {self.nome}:")
        print(f"Vida: {self.vida}")
        print(f"Força: {self.forca}")
        print(f"Defesa: {self.defesa}")
        print(f"XP: {self.xp}\n")

    def mudar_personagem(self, novo_personagem):
        self.nome = novo_personagem.nome
        self.vida = novo_personagem.vida
        self.forca = novo_personagem.forca
        self.defesa = novo_personagem.defesa

    def dar_dano_inimigo(self, monstro):
        dano = min(self.forca, monstro["vida"])
        monstro["vida"] -= dano
        print(f"Você causou {dano} de dano ao monstro!")

    def sofrer_dano(self, inimigo):
        if isinstance(inimigo, dict):
            dano = max(0, inimigo["forca"] - self.defesa)
            self.vida -= dano
            print(f"Você sofreu {dano} de dano do monstro.")
        elif isinstance(inimigo, int):
            self.vida -= inimigo
            print(f"Você sofreu {inimigo} de dano da armadilha.")

    def ganhar_recompensa(self):
        self.xp += 15
        print(self.xp)
        self.vida += 10
        self.forca += 5
        self.defesa += 5
