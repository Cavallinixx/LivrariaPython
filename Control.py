from MenuLivro import MenuLivro
class Control:

    def __init__(self):
        self.loginUm = ""
        self.senhaUm = ""
        self.login2 = "vitor"
        self.senha2 = "123"
        self.exer = MenuLivro()



    def validarLogin(self):
        if((self.loginUm == self.login2) & ( self.senhaUm == self.senha2)):
          return f"Seja bem vindo!{self.exer.menuLivro()}"
        else:
          return f"Dados incorretos, digite novamente!"








