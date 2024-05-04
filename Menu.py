from Control import Control

class Menu:
    def __init__(self):
        self.opcao = -1
        self.exer = Control()

    def login(self):
        self.exer.loginUm = input("Informe seu login: ")
        self.exer.senhaUm = input("Informe sua senha: ")

    def cadastro(self):
        self.exer.login = input("Informe o login: ")
        self.exer.senha = input("Informe a senha: ")
        self.exer.login = input("Informe o endereço: ")
        self.exer.senha = input("Informe o telefone: ")
        self.exer.login = input("Informe a data de nascimento: ")
        self.exer.senha = input("Informe o nome: ")
        print("Cadastro feito com sucesso!")


    def menuInicio(self):
        self.opcao = int(input("-----Menu-----\n\n" +
                               "\n0. Sair      "    +
                               "\n1. Entrar    "    +
                               "\n2. Cadastrar "    +
                               "\nEscolha uma das opções acima: "))

    def operacao(self):
        while(self.opcao != 0):
            self.menuInicio()
            if(self.opcao == 0):
                print("Obrigado!")
            elif(self.opcao == 1):
                self.login()
                print(self.exer.validarLogin())
            elif (self.opcao == 2):
                self.cadastro()

            else:
                print("Código escolhido não é valido!")



