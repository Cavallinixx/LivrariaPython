from ControlLivro import ControlLivro
from Compra import Compra

class MenuLivro:

    def __init__(self):
        self.opcao = -1
        self.exer = ControlLivro()
        self.exer = Compra()


    def menuLivro(self):
        self.opcao = int(input("-----Menu-----\n\n" +
                               "\n0. Sair " +
                               "\n1. Cabeça Fria Coração Quente - R$68,90 " +
                               "\n2. LeBron  -                    R$78,90" +
                               "\n3. Elon Musk -                  R$77,50" +
                               "\n4. Messi: O Gênio Completo -    R$55,90" +
                               "\nEscolha uma das opções acima: "))


    def operacao(self):
        while (self.opcao != 0):
            self.menuLivro()
            if (self.opcao == 0):
                print("Obrigado!")
            elif (self.opcao == 1):
                self.exer.pagamento()

            elif (self.opcao == 2):
                self.exer.pagamento()

            elif (self.opcao == 3):
                self.exer.pagamento()

            elif (self.opcao == 4):
                self.exer.pagamento()

            else:
                print("Código escolhido não é valido!")

