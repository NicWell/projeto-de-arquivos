from cliente import Cliente
from funcionario import Funcionario

nome = 'Pedro'
cpf = 13914163410
senha = 223
teste = Funcionario(nome, cpf, senha)
teste.atualiza_func(nome, cpf, senha)