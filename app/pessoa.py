class Pessoa():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.tipoPessoa = self.__class__.__name__