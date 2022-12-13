from pessoa import Pessoa
import re

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