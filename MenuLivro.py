from Reserva import Reserva
class MenuLivro:
    def __init__(self):
        self.opcao = -1
        self.exer = Reserva()

    def menuLivro(self):
        self.opcao = int(input("-----Menu-----\n\n" +
                               "\n0. Sair " +
                               "\n1. Cabeça Fria Coração Quente - R$68,90 " +
                               "\n2. LeBron  -                    R$78,90" +
                               "\n3. Elon Musk -                  R$77,50" +
                               "\n4. Messi: O Gênio Completo -    R$55,90" +
                               "\n5. Realizar Reserva " +
                               "\nEscolha uma das opções acima: "))

    def pagamento(self):
        if self.opcao == 0:
            print("Obrigado!")
        elif self.opcao == 1:
            return "Você escolheu o livro: Cabeça Fria Coração Quente, R$68,90"
        elif self.opcao == 2:
            return "Você escolheu o livro: LeBron, R$78,90"
        elif self.opcao == 3:
            return "Você escolheu o livro: Elon Musk, R$77,50"
        elif self.opcao == 4:
            return "Você escolheu o livro: Messi: O Gênio Completo, R$55,90"
        elif self.opcao == 5:
            return f"{self.exer.menuReserva()}"

    def operacao(self):
        self.menuLivro()
        resultado = self.pagamento()
        return resultado