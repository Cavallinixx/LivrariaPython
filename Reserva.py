class Reserva:
    def __init__(self):
        self.reservas = {}
        self.opcao = -1

    def realizarReserva(self, livro, quantidade):
        if livro in self.reservas:
            self.reservas[livro] += quantidade
        else:
            self.reservas[livro] = quantidade

    def cancelarReserva(self, livro, quantidade):
        if livro in self.reservas:
            self.reservas[livro] -= quantidade
            if self.reservas[livro] <= 0:
                del self.reservas[livro]
        else:
            print("Reserva não encontrada.")

    def listarReservas(self):
        print("Reservas:")
        for livro, quantidade in self.reservas.items():
            print(f"{livro}: {quantidade} unidades")

    def menuReserva(self):
        self.opcao = int(input("-----Menu-----\n\n" +
                               "\n0. Sair " +
                               "\n1. Realizar reserva " +
                               "\n2. Cancelar reserva " +
                               "\n3. Listar reservas " +
                               "\nEscolha uma das opções acima: "))

    def operacaoReserva(self):
        while self.opcao != 0:
            self.menuReserva()
            if self.opcao == 0:
                print("Obrigado!")
            elif self.opcao == 1:
                livro = input("Digite o nome do livro: ")
                quantidade = int(input("Digite a quantidade a ser reservada: "))
                self.realizarReserva(livro, quantidade)
            elif self.opcao == 2:
                livro = input("Digite o nome do livro: ")
                quantidade = int(input("Digite a quantidade a ser cancelada: "))
                self.cancelarReserva(livro, quantidade)
            elif self.opcao == 3:
                self.listarReservas()
            else:
                print("Número informado não foi encontrado!")