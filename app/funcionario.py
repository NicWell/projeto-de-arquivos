from pessoa import Pessoa
import re
import time

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, senha):
        super().__init__(nome, cpf)
        self._senha = senha
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
    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, senha):
        self._senha = senha

    def cadastra_func(self):
        if('Funcionarios') not in self._Dados:
            self._Dados['Funcionarios'] = {self._cpf: self._nome, 'senha':self._senha}
        else:
            self._Dados['Funcionarios'].update({self._cpf: self._nome, 'senha':self._senha})
        for cpf,nome in self._Dados['Funcionarios'].items():
            with open('./base/funcionario.txt', 'a+', encoding='utf-8') as add:
                add.write(str(cpf)+':')
                add.write(str(nome)+"\n")
        print("Funcionario Cadastrado!!")
    def deleta_func(self,cpf):
        usrAt = []
        with open('base/funcionario.txt', 'r') as usRead:
            for line in usRead:
                usrAt.append(str(line.strip()))
        #print(usrAt)
        pos = None
        for x in range(0, len(usrAt)):
            if(re.search(str(cpf), usrAt[x])):
                pos = x
        if (pos != None):
            del(usrAt[pos])
            del(usrAt[pos])
            print("FUNCIONÁRIO DELETADO!!")
        else:
            print("Não foi possível Deletar o registro, ele não se encontra no sistema!")
        with open('base/funcionario.txt', 'w', encoding= 'utf-8') as update:
            for x in range(0, len(usrAt)):
                update.write(str(usrAt[x])+'\n')
    def lista_func(self):
        listFunc = []
        with open('base/funcionario.txt', 'r') as read:
            for line in read:
                listFunc.append(str(line.strip()))
        for x in range(0, len(listFunc)):
            listFunc[x] = str(listFunc[x]).split(':')
        for x in range(0, len(listFunc)):
            for y in listFunc[x]:
                listFunc[x] = y
        listNomes = []
        for x in range(0, len(listFunc)):
            if (x%2 == 0):
                listNomes.append(listFunc[x]) 
        time.sleep(1)
        print("\nLISTA DE FUNCIONARIOS:\n")
        y = 1
        for x in range(0, len(listNomes)):
            time.sleep(0.5)
            print(str(y)+" - "+listNomes[x])
            print('--------------------------------')
            y+=1
    def atualiza_func(self, nome, cpf, senha):
        listaFunc = []
        with open('base/funcionario.txt', 'r') as readF:
            for line in readF:
                listaFunc.append(str(line.strip()))
        pos = None
        for x in range(0, len(listaFunc)):
            if(re.search(str(cpf), listaFunc[x]) or re.search(nome, listaFunc[x])):
                pos = x
        if (pos != None):
            listaFunc[pos] = str(cpf)+':'+nome
            pos += 1
            listaFunc[pos] = 'senha:'+str(senha)
            print('--------------------------------')
            print("Funcionário atualizado!!")
            print('--------------------------------')
            with open('base/funcionario.txt', 'w', encoding= 'utf-8') as update:
                for x in range(0, len(listaFunc)):
                    update.write(str(listaFunc[x])+'\n')
        else:
            print("Não foi possível Atualizar o registro, ele não se encontra no sistema!")