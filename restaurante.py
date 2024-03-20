class Nodo:
    def __init__(self, dado=0, proximoNodo=None):
        self.dado = dado
        self.proximo = proximoNodo

    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'

    def setProximo(self, proximoNodo):
        self.proximo = proximoNodo


class Cliente:
    def __init__(self, nome, valorDaConta):
        self.nome = nome
        self.valorDaConta = valorDaConta

    def __repr__(self):
        return f'{self.nome} -> {self.valorDaConta}'


class ListaSimplesmenteEncadeada:
    def __init__(self):
        self.head = None
        self.tamanhoDaLista = 0
        self.somaDosValores = 0  # Soma dos valores das contas

    def insere(self, novoDado):
        novoNodo = Nodo(novoDado)
        novoNodo.proximo = self.head
        self.head = novoNodo
        self.tamanhoDaLista += 1

        # Atualiza a soma dos valores das contas
        self.somaDosValores += novoDado.valorDaConta

    def delete(self):
        if self.head is None:
            print('A lista já está vazia')
        else:
            # Atualiza a soma dos valores das contas ao excluir um cliente
            self.somaDosValores -= self.head.dado.valorDaConta
            self.head = self.head.proximo
            self.tamanhoDaLista -= 1

    def calcular_media(self):
        if self.tamanhoDaLista == 0:
            return 0
        else:
            return self.somaDosValores / self.tamanhoDaLista


# Exemplo de uso
lista_clientes = ListaSimplesmenteEncadeada()

# Adicionando alguns clientes
lista_clientes.insere(Cliente("Cliente 1", 100))
lista_clientes.insere(Cliente("Cliente 2", 200))
lista_clientes.insere(Cliente("Cliente 3", 150))

# Calculando e imprimindo a média
media = lista_clientes.calcular_media()
print("Média dos valores das contas:", media)

# Removendo um cliente
lista_clientes.delete()

# Calculando e imprimindo a nova média
media = lista_clientes.calcular_media()
print("Nova média após a remoção de um cliente:", media)
