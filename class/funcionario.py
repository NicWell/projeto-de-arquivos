from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, idade):
        super().__init__(nome, cpf, idade)
