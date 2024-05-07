from MenuLivro import MenuLivro

class Menu:
    def __init__(self):
        self.opcao = -1
        self.loginUm = ""
        self.senhaUm = ""
        self.login2 = "vitor"
        self.senha2 = "123"
        self.exer = MenuLivro()




    def cadastro(self):
        self.exer.login = input("Informe o login: ")
        self.exer.senha = input("Informe a senha: ")
        self.exer.login = input("Informe o endereço: ")
        self.exer.senha = input("Informe o telefone: ")
        self.exer.login = input("Informe a data de nascimento: ")
        self.exer.senha = input("Informe o nome: ")
        print("Cadastro feito com sucesso!")

    def validarLogin(self):
        while True:  # Loop infinito
            self.loginUm = input("Informe seu login: ")
            self.senhaUm = input("Informe sua senha: ")

            if self.loginUm == self.login2 and self.senhaUm == self.senha2:
                return "Seja bem vindo!" and print(self.exer.menuLivro())
            else:
                print("Dados incorretos, digite novamente!")


    def menuInicio(self):
        self.opcao = int(input("-----Menu-----\n\n" +
                               "\n0. Sair      "    +
                               "\n1. Entrar    "    +
                               "\n2. Cadastrar "    +
                               "\nEscolha uma das opções acima: "))

    def operacaoMenu(self):
        while(self.opcao != 0):
            self.menuInicio()
            if(self.opcao == 0):
                print("Obrigado!")
            elif(self.opcao == 1):
                self.validarLogin()
            elif (self.opcao == 2):
                self.cadastro()

            else:
                print("Código escolhido não é valido!")





