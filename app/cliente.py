from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self._Dados = {}
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    def listaRecent(self):
        print(f'Cliente novo é {self._nome}')
        print(self._Dados.items())

    def cadastra_cliente(self):
        if('Clientes') not in self._Dados:
            self._Dados['Clientes'] = {self._cpf: self._nome}
        else:
            self._Dados['Clientes'].update({self._cpf: self._nome})
        for cpf, nome in self._Dados['Clientes'].items():
            with open('./base/cliente.txt', 'a+', encoding='utf-8') as add:
                add.write(str(cpf)+':')
                add.write(str(nome)+"\n")
        print("Cliente Cadastrado!!")