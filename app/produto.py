import time

class Produto():
    def __init__(self, nome, estoque, valor):
        self._nome = nome
        self._estoque = estoque
        self._valor = valor
        self.__idProd = None
    @property
    def idProd(self):
        return self.__idProd
    @idProd.setter
    def idProd(self, value):
        self.__idProd = value
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    @property
    def estoque(self):
        return self._estoque
    @estoque.setter
    def estoque(self, estoque):
        self._estoque = estoque
    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, valor):
        self._valor = valor
    def cadasta_Produto(self, nome, estoque, valor):
        with open('./base/idProd.txt', 'r', encoding='utf-8') as read:
            self.__idProd = read.readline()
        with open('base/produto.txt', 'a+') as add:
            add.write(str(self.__idProd)+":"+nome)
            add.write("\nvalor:"+str(valor)+"\n")
        with open('base/produtoEstoque.txt', 'a+') as add:
            add.write("id:"+str(self.__idProd))
            add.write("\nestoque:"+str(estoque)+"\n")
        #finally
        id = int(self.__idProd)
        id+=1
        with open('./base/idProd.txt', 'w', encoding='utf-8') as read:
            read.write(str(id))
        print("Produto Cadastrado!!")
    def lista_Produto(self):
        listaProdV = []
        listaProdQ = []
        with open('base/produtoEstoque.txt', 'r') as read:
            for line in read:
                listaProdQ.append(str(line.strip()))
        with open('base/produto.txt', 'r') as read:
            for line in read:
                listaProdV.append(str(line.strip()))
        print("Estoque")
        print(listaProdQ)
        print("VAlor")
        print(listaProdV)

