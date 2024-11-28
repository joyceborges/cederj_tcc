class ProjectView():

    def __init__(self) -> None:
        pass

    @staticmethod
    

    @staticmethod
    def get_user_choice_menu():
        while True:
            msg_prompt = "Escolha uma opção de (1-4): "
            try:
                choice = int(input(msg_prompt))
                if choice in range(1, 6):
                    return choice
                else:
                    print(f"Escolha inválida. {msg_prompt}")
            except ValueError:
                print(f"Escolha inválida. {msg_prompt}")

    @staticmethod
    def get_user_choice_model():
        while True:
            try:
                choice = int(input("Digite o número do modelo a ser utilizado no projeto: "))
                return choice
            except ValueError:
                print("Valor inválido. Por favor, digite um número válido.")


if __name__ == '__main__':
    print('end')