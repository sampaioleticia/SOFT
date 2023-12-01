import pytest
from usuario import Usuario


def test_fazer_login_correto():
    usuario = Usuario("Nome", 1, "login", "senha", "email@example.com")
    assert usuario.fazer_login("login", "senha") is True


def test_fazer_login_incorreto():
    usuario = Usuario("Nome", 1, "login", "senha", "email@example.com")
    assert usuario.fazer_login("login", "senha_incorreta") is False


def test_fazer_cadastro_login_disponivel():
    usuario_existente = Usuario(
        "Nome", 1, "login_existente", "senha", "email@example.com")
    novo_usuario = usuario_existente.fazer_cadastro(
        "Novo Nome", 2, "novo_login", "nova_senha", "novo_email@example.com")
    assert novo_usuario.login == "novo_login"


def test_fazer_cadastro_login_existente():
    usuario_existente = Usuario(
        "Nome", 1, "login_existente", "senha", "email@example.com")
    with pytest.raises(ValueError, match="Login já existente. Escolha outro login."):
        usuario_existente.fazer_cadastro(
            "Novo Nome", 2, "login_existente", "nova_senha", "novo_email@example.com")


def test_login_disponivel():
    usuario_existente = Usuario(
        "Nome", 1, "login_existente", "senha", "email@example.com")
    assert usuario_existente.login_disponivel("novo_login") is True
    assert usuario_existente.login_disponivel("login_existente") is False
