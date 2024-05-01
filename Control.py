class Control:

    def __init__(self):
        self.login = ""
        self.senha = ""
        self.usuario = self.login + self.senha
    def login(self):

        if(self.login & self.senha != self.usuario ):
            return f"O login ou senha estão incorretos!"
        else:
            return f"Bem vindo!"




