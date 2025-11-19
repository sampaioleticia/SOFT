class Usuario:
    def __init__(self, nome, ide, login, senha, email, personagem_selecionado=None):
        self.nome = nome
        self.ide = ide
        self.login = login
        self.senha = senha
        self.email = email
        self.personagem_selecionado = personagem_selecionado

    def fazer_login(self, login, senha):
        return self.login == login and self.senha == senha

    def fazer_cadastro(self, nome, ide, login, senha, email, personagem_selecionado=None):
        if self.login_disponivel(login):
            novo_usuario = Usuario(
                nome, ide, login, senha, email, personagem_selecionado)
            return novo_usuario
        else:
            raise ValueError("Login já existente. Escolha outro login.")

    def login_disponivel(self, login):
        return login != self.login