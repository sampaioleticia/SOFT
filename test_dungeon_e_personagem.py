import pytest
from personagem import Personagem
from dungeon import Dungeon


@pytest.fixture
def sample_personagem():
    return Personagem("Herói", forca=10, defesa=5)


@pytest.fixture
def sample_dungeon():
    return Dungeon()


def test_personagem_criacao():
    personagem = Personagem("Mago", forca=10, defesa=5)
    assert personagem.nome == "Mago"
    assert personagem.forca == 10
    assert personagem.defesa == 5
    assert personagem.vida == 100
    assert personagem.xp == 0


def test_personagem_mudar_personagem(sample_personagem):
    novo_personagem = Personagem("Druida", forca=15, defesa=8)
    sample_personagem.mudar_personagem(novo_personagem)
    assert sample_personagem.nome == "Druida"
    assert sample_personagem.forca == 15
    assert sample_personagem.defesa == 8


def test_personagem_dar_dano_inimigo(sample_personagem):
    monstro = {"vida": 50}
    sample_personagem.dar_dano_inimigo(monstro)
    assert monstro["vida"] < 50


def test_personagem_sofrer_dano_monstro(sample_personagem):
    inimigo = {"forca": 15}
    initial_health = sample_personagem.vida
    sample_personagem.sofrer_dano(inimigo)
    assert sample_personagem.vida < initial_health


def test_personagem_sofrer_dano_armadilha(sample_personagem):
    damage = 10
    initial_health = sample_personagem.vida
    sample_personagem.sofrer_dano(damage)
    assert sample_personagem.vida < initial_health


def test_personagem_ganhar_recompensa(sample_personagem):
    initial_xp = sample_personagem.xp
    initial_health = sample_personagem.vida
    initial_strength = sample_personagem.forca
    initial_defense = sample_personagem.defesa

    sample_personagem.ganhar_recompensa()

    assert sample_personagem.xp == initial_xp + 15
    assert sample_personagem.vida == initial_health + 10
    assert sample_personagem.forca == initial_strength + 5
    assert sample_personagem.defesa == initial_defense + 5


def test_dungeon_iniciar_dungeon(sample_dungeon):
    sample_dungeon.iniciar_dungeon()
    assert len(sample_dungeon.monstros) == 5
    assert len(sample_dungeon.armadilhas) == 5


def test_dungeon_resolver_problema_dungeon(sample_dungeon, sample_personagem, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 'a, b = b, a')
    sample_dungeon.iniciar_dungeon()
    sample_dungeon.posicao_atual = 2
    sample_dungeon.monstros[2] = {"vida": 50, "forca": 10, "defesa": 5}

    sample_dungeon.resolver_problema_dungeon(sample_personagem)


def test_dungeon_mover_direita(sample_dungeon, sample_personagem):
    initial_position = sample_dungeon.posicao_atual
    sample_dungeon.mover_direita(sample_personagem)
    assert sample_dungeon.posicao_atual == initial_position + 1


def test_dungeon_mover_esquerda(sample_dungeon, sample_personagem):
    initial_position = sample_dungeon.posicao_atual
    sample_dungeon.mover_esquerda(sample_personagem)
    assert sample_dungeon.posicao_atual == initial_position - 1


def test_dungeon_dar_dano_monstro_especial(sample_dungeon, sample_personagem, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 'a, b = b, a')
    sample_dungeon.iniciar_dungeon()
    sample_dungeon.posicao_atual = 25
    sample_dungeon.monstros[25] = {"vida": 50, "forca": 15, "defesa": 15}

    sample_dungeon.dar_dano_monstro_especial(sample_personagem)


def test_dungeon_dar_dano_armadilha_pouca_saude(sample_dungeon, sample_personagem, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 'resposta_errada')
    sample_dungeon.iniciar_dungeon()
    sample_dungeon.posicao_atual = 3
    sample_personagem.vida = 5

    sample_dungeon.dar_dano_armadilha(
        sample_dungeon.posicao_atual, sample_personagem)


def test_dungeon_mover_direcao_errada(sample_dungeon, sample_personagem, capsys):
    sample_dungeon.mover("direcao_errada", sample_personagem)
    captured = capsys.readouterr()
    assert "Comando inválido!" in captured.out


if __name__ == "__main__":
    pytest.main()
