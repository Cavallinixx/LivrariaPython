from Control import Control

class Menu:
    def __init__(self):
        self.opcao = -1
        self.exer = Control()

    def login(self):
        self.exer.login = input("Informe seu login: ")
        self.exer.senha = input("Informe sua senha: ")


    def menuInicio(self):
        self.opcao = int(input("-----Menu-----\n\n" +
                               "\n0. Sair      "    +
                               "\n1. Entrar    "    +
                               "\n2. Cadastrar "    +
                               "\nEscolha uma das opções acima:"))


    def operacao(self):
        while(self.opcao != 0):
            self.menuInicio()
            if(self.opcao == 0):
                print("Obrigado!")
            elif(self.opcao == 1):
                self.login()
                print(self.exer.login())
            elif (self.opcao == 2):
                self.coletar()
                print(self.exer.cadastro())
            else:
                print("Código escolhido não é valido!")
