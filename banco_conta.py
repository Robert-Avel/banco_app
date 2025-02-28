from abc import ABC, abstractmethod
from random import randint
import cliente
class Banco:
    def __init__(self, nome: str):
        self.nome = nome
        self.contas: list[cliente.Cliente] = []
        self.agencias: list[int] = []
        
    

    def __str__(self):
        return f'{self.nome}({len(self.contas)} contas)'
    

    def __repr__(self):
        return f'{__class__.__name__}({repr(self.nome)})'
    

    def cadastrar_cliente(self, nome, idade, conta):
        novo_client = cliente.Cliente(nome, idade, conta, self)
        self.contas.append(novo_client)


    def fechar_conta(self):
        from meu_modulo import inputRange, pergunta
        if not self.contas:
            print(f'---> Não existem contas abertas no Banco "{self.nome}"')
            return
        for n, c in enumerate(self.contas):
            print(f'[ {n} ] - {c}')
        client = inputRange('Escolha o cliente que deseja apagar a conta', self.contas)
        p = pergunta(f'Quer mesmo apagar a conta de {self.contas[client]} ?')
        if p:
            print(f'{self.contas[client]} Deletado com sucesso')
            del self.contas[client]
        

    def editar_conta(self):
        from meu_modulo import inputInt, inputRange
        if not self.contas:
            print(f'---> Não existem contas abertas no Banco "{self.nome}"')
            return
        for n, c in enumerate(self.contas):
            print(f'[ {n} ] - {c}')
        client = inputRange('Escolha o cliente que deseja editar: ', self.contas)
        new_name = str(input('Novo Nome:'))
        new_age = inputInt('Nova idade: ')
        self.contas[client]._nome = new_name
        self.contas[client]._idade = new_age


class Conta(ABC):
    @abstractmethod
    def __init__(self, banco):
        self.agencia = randint(100, 999)
        self.saldo = 0.0
        self.conta = None
        self._banco = Banco(banco)
    

    @abstractmethod
    def sacar(self, valor: float):
        return
    

    def depositar(self, valor: float):
        self.saldo += valor
        print(f'Você depositou um valor de R${valor:.2f}, seu saldo atual ficou R${self.saldo:.2f}')
    

    def __str__(self):
        return f'Agencia: {self.agencia} \nConta: {self.conta} \nSaldo: R${self.saldo:.2f} \nBanco: {self._banco.nome}'


    def __repr__(self):
        return f'{__class__.__name__}({repr(self._banco)})'

class ContaCorrente(Conta):
    def __init__(self, banco):
        super().__init__(banco)
        self.conta = 'Corrente'
    

    def sacar(self, valor):
        if self.saldo - valor < -100:
            print(f'O limite do seu saldo está abaixo de R${valor}, não foi possivel sacar')
        elif self.saldo - valor < 0:
            self.saldo -= valor
            print(f'Você sacou um valor de R${valor:.2f}, seu saldo atual ficou R${self.saldo:.2f}\n \
                  Você ficou devendo R${self.saldo*-1}')
        else:
            self.saldo -= valor
            print(f'Você sacou um valor de R${valor:.2f}, seu saldo atual ficou R${self.saldo:.2f}')


class ContaPoupança(Conta):
    def __init__(self, banco):
        super().__init__(banco)
        self.conta = 'Poupança'
    

    def sacar(self, valor):
        if self.saldo - valor < 0:
            print(f'Seu saldo está abaixo de R${valor}, não foi possivel sacar')
        else:
            self.saldo -= valor
            print(f'Você sacou um valor de R${valor:.2f}, seu saldo atual ficou R${self.saldo:.2f}')


if __name__ == '__main__':
    b1 = Banco('Bradescco')
    print(repr(b1))

    b1.cadastrar_cliente('Eli', 23, 'C')
    print(b1.__dict__)