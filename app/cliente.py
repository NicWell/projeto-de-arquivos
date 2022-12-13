from pessoa import Pessoa
import re
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
    '''
    def listaRecent(self):
        print(f'Cliente novo é {self._nome}')
        print(self._Dados.items())
    '''

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
    def deleta_cliente(self, cpf):
        usrAt = []
        with open('base/cliente.txt', 'r') as usRead:
            for line in usRead:
                usrAt.append(str(line.strip()))
        #print(usrAt)
        pos = None
        for x in range(0, len(usrAt)):
            if(re.search(str(cpf), usrAt[x])):
                pos = x
        if (pos != None):
            del(usrAt[pos])
            print("Registro Deletado")
        else:
            print("Não foi possível Deletar o registro, ele não se encontra no sistema!")
        with open('base/cliente.txt', 'w', encoding= 'utf-8') as update:
            for x in range(0, len(usrAt)):
                update.write(str(usrAt[x])+'\n')
    def lista_Clientes(self):
        listClientes = []
        with open('base/cliente.txt', 'r') as readCliente:
            for line in readCliente:
                listClientes.append(str(line.strip()))
        for x in range(0, len(listClientes)):
            listClientes[x] = str(listClientes[x]).split(':')
        print(listClientes)
        for x in range(0, len(listClientes)):
            for y in listClientes[x]:
                listClientes[x] = y
        print("\nLISTA DE CLIENTES:\n")
        for nomes in listClientes:
            print(nomes)
            print('--------------------------------')
    def atualiza_Clientes(self, cpf, nome):
        listClientes = []
        with open('base/cliente.txt', 'r') as readCliente:
            for line in readCliente:
                listClientes.append(str(line.strip()))
        print(listClientes)
        pos = None
        for x in range(0, len(listClientes)):
            if(re.search(str(cpf), listClientes[x])):
                pos = x
        if (pos != None):
            listClientes[pos] = str(cpf)+':'+str(nome)
            print(listClientes)
            print('--------------------------------')
            print("Cliente atualizado!!")
            print('--------------------------------')
            with open('base/cliente.txt', 'w', encoding= 'utf-8') as update:
                for x in range(0, len(listClientes)):
                    update.write(str(listClientes[x])+'\n')
        else:
            print("Não foi possível Atualizar o registro, ele não se encontra no sistema!")