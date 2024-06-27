class Reserva:
    def __init__(self, nome, data, hora):
        self.nome = nome
        self.data = data
        self.hora = hora

    def __str__(self):
        return f"Reserva para {self.nome} em {self.data} às {self.hora}"

class SistemaReservas:
    def __init__(self):
        self.reservas = []

    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)
        print(f"Reserva adicionada: {reserva}")

    def exibir_reservas(self):
        if not self.reservas:
            print("Não há reservas.")
        else:
            for reserva in self.reservas:
                print(reserva)

    def cancelar_reserva(self, nome, data, hora):
        for reserva in self.reservas:
            if reserva.nome == nome and reserva.data == data and reserva.hora == hora:
                self.reservas.remove(reserva)
                print(f"Reserva cancelada: {reserva}")
                return
        print("Reserva não encontrada.")


def menu():
    sistema = SistemaReservas()

    while True:
        print("\nSistema de Reservas")
        print("1. Adicionar Reserva")
        print("2. Exibir Reservas")
        print("3. Cancelar Reserva")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            data = input("Data (DD/MM/AAAA): ")
            hora = input("Hora (HH:MM): ")
            reserva = Reserva(nome, data, hora)
            sistema.adicionar_reserva(reserva)
        elif escolha == '2':
            sistema.exibir_reservas()
        elif escolha == '3':
            nome = input("Nome: ")
            data = input("Data (DD/MM/AAAA): ")
            hora = input("Hora (HH:MM): ")
            sistema.cancelar_reserva(nome, data, hora)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
