from Menu import Menu
from Reserva import Reserva

if __name__ == '__main__':
    controle = Menu()
    controle.operacaoMenu()
    reservas = Reserva()
    reservas.realizarReserva("Cabeça Fria Coração Quente", 1)
    reservas.realizarReserva("LeBron", 1)
    reservas.listarReservas()
    reservas.cancelarReserva("Cabeça Fria Coração Quente", 1)
    reservas.listarReservas()
    reserva = Reserva()
    reserva.operacaoReserva()




