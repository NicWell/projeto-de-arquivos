
from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, cpf):
        self._Dados = {
            'Clientes':{
                self.cfp: self.nome
            }
        }
        super().__init__(nome, cpf)
       

    def cadastra_cliente(self, nome, cpf):
        if('Clientes') not in self._Dados:
            self._Dados['Clientes'] = {cpf: nome}
        else:
            self._Dados['Clientes'].update({cpf: nome})
    def listaClientes(self):
        print("Lista de clientes...")
        for _, nome in self._Dados['Clientes'].iteritems():
            print(nome)
'''
teste = Cliente("well", "192919929919", 26)
print(f'{teste.nome} É um {teste.tipoPessoa}')
'''