from abc import ABC, abstractmethod
import banco_conta
class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade
    

    def __str__(self):
        return f'{self._nome} ({self._idade} anos)'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta: str, banco):
        super().__init__(nome, idade)
        if conta.startswith(('P', 'p')):
            self.conta = banco_conta.ContaPoupança(banco)
        elif conta.startswith(('C', 'c')):
            self.conta = banco_conta.ContaCorrente(banco)
        else:
            raise ValueError('Valor de conta incorreto.')


    def __repr__(self):
        super().__init__(self._nome, self._idade)
        return f'{__class__.__name__}({repr(self._nome)}, {self._idade}, {repr(self.conta)})'


if __name__ == '__main__':
    cl1 = Cliente('Joel', 22, 'Corrente', banco_conta.Banco('blalablba'))
    print(str(cl1))
    cl1.conta.depositar(123423)
    print(repr(cl1))