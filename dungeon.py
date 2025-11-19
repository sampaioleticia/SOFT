import random
import math
from personagem import Personagem

class Dungeon:
    def __init__(self):
        self.posicao_atual = 0
        self.monstros = {}
        self.armadilhas = {}

    def iniciar_dungeon(self):
        self._gerar_monstros_e_armadilhas()

    def _gerar_monstros_e_armadilhas(self):
        for i in range(5):
            self.monstros[i * 5 + 2] = {"vida": random.randint(50, 100),
                                        "forca": random.randint(5, 10),
                                        "defesa": random.randint(5, 10)}
            self.armadilhas[i * 5 + 3] = {"dano": random.randint(10, 20)}

    def gerar_problema(self):
        problemas = {
            "Como podemos trocar os valores de duas variáveis sem usar uma variável temporária?": ("Pense em como você pode usar a aritmética básica para realizar essa troca diretamente.", "a, b = b, a"),
            "Como podemos inverter uma lista em Python?": ("Pense em como os índices podem ser usados para acessar os elementos de uma lista de trás para frente.", "lista_invertida = lista[::-1]"),
            "Como podemos verificar se uma string é um palíndromo em Python?": ("Pense em como você pode comparar a string original com sua versão invertida.", "def eh_palindromo(s): return s == s[::-1]"),
            "Como podemos somar todos os números em uma lista em Python?": ("Considere o uso de um loop para percorrer todos os elementos da lista e acumular a soma.", "soma = sum(lista)"),
            "Como podemos encontrar o maior elemento em uma lista em Python?": ("Pense em como você pode percorrer a lista e manter o controle do maior valor encontrado.", "maior_elemento = max(lista)"),
        }
        problema = random.choice(list(problemas.keys()))
        dica, resposta_correta = problemas[problema]
        return problema, dica, resposta_correta

    def resolver_problema_dungeon(self, personagem):
        problema, dica, resposta_correta = self.gerar_problema()
        print(
            f"Nobre heroí, resolva o problema de computação para batalhar: {problema}")
        resposta_usuario = input("Sua resposta: ")

        if resposta_usuario == resposta_correta:
            personagem.dar_dano_inimigo(self.monstros[self.posicao_atual])
            print("Parabéns herói, você acertou! Você deu dano ao monstro.")
        else:
            personagem.sofrer_dano(self.monstros[self.posicao_atual])
            print("Que pena, você errou! O monstro atacou e causou dano a você.")

    def dar_dano_armadilha(self, posicao, personagem):
        armadilha = self.armadilhas[posicao]
        problema, dica, resposta_correta = self.gerar_problema()
        print(f"Você caiu em uma armadilha! Resolva o problema para reduzir o dano pela metade.")
        print(f"Problema: {problema}")
        resposta_usuario = input("Sua resposta: ")

        if resposta_usuario == resposta_correta:
            personagem.sofrer_dano(armadilha["dano"] // 2)
            print(
                f"Parabéns herói, você acertou! Sofreu apenas {armadilha['dano'] // 2} de dano.")
        else:
            personagem.sofrer_dano(armadilha["dano"])
            print(f"Que pena, você errou! Sofreu {armadilha['dano']} de dano.")

    def mover(self, direcao, personagem):
        if direcao == "hero.moveRight()":
            self.mover_direita(personagem)
        elif direcao == "hero.moveLeft()":
            self.mover_esquerda(personagem)
        else:
            print("Comando inválido! Use 'hero.moveRight()' ou 'hero.moveLeft()'.")

    def mover_direita(self, personagem):
        self.posicao_atual += 1
        if self.posicao_atual in self.monstros:
            self.dar_dano_monstro(self.posicao_atual, personagem)
        elif self.posicao_atual in self.armadilhas:
            self.dar_dano_armadilha(self.posicao_atual, personagem)

    def mover_esquerda(self, personagem):
        self.posicao_atual -= 1
        if self.posicao_atual in self.monstros:
            self.dar_dano_monstro(self.posicao_atual, personagem)
        elif self.posicao_atual in self.armadilhas:
            self.dar_dano_armadilha(self.posicao_atual, personagem)

    def dar_dano_monstro_especial(self, personagem):
        monstro_especial = self.monstros[25]
        problema, dica, resposta_correta = self.gerar_problema()
        print(f"Você encontrou o MONSTRO ESPECIAL! Resolva o problema para causar dano.")
        print(f"Problema: {problema}")
        resposta_usuario = input("Sua resposta: ")

        if resposta_usuario == resposta_correta:
            personagem.dar_dano_inimigo(monstro_especial)
            print("Parabéns herói, você acertou! Você deu dano ao Monstro Especial.")
        else:
            personagem.sofrer_dano({"forca": 15, "defesa": 15, "vida": 50})
            print("Que pena, você errou! O monstro especial atacou e causou dano a você.")

        if monstro_especial["vida"] <= 0:
            personagem.ganhar_recompensa()
            self.finalizar_dungeon(personagem)
        else:
            print(f"Vida do monstro especial: {monstro_especial['vida']}")

    def finalizar_dungeon(self, personagem):
        if personagem.vida > 0:
            print("Parabéns herói! Você terminou a dungeon!")
            print(f"XP acumulado: {personagem.xp}")
        else:
            print("Você morreu, mas não desanime! Tente novamente")
            self.iniciar_dungeon()
