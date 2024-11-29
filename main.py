from project_controller import ProjectController
from pandas import DataFrame as pd

# Para exemplificar o controller:
from unittest.mock import patch

def display_initial_menu():
        """
        Displays the menu options to the user.
        """
        print("\n===========MENU============")
        print("1. Criar um novo projeto")
        print("2. Selecionar um projeto já existente")
        print("=============================")

def display_project_menu():
        """
        Displays the menu options to the user.
        """
        print("\n===========MENU============")
        print("A. Treinar um novo modelo")
        print("B. Testar um modelo")
        print("C. Usar um modelo para fazer um predict")
        print("=============================")

def main():
    ctrl = ProjectController()
    
    # Enquanto não houver um projeto selecionado, continue exibindo o menu
    while ctrl._project is None:
    
        display_initial_menu()
        choice = int(input("Escolha uma opção (1 ou 2): "))

        if choice == 1:

            name = input("Nome do projeto: ")
            description = input("Descrição do projeto: ")
            
            # Lista os modelos disponíveis
            print('Escolha pelo índice o modelo desejado. Modelos disponíveis:')
            models = ctrl._list_folders(folder_name = 'models_ia')
            print(models)
            model = int(input("Modelo do projeto (número): "))

            # Cria um novo projeto
            project_selected = ctrl.create_project(name, description, model)

        elif choice == 2:
                '''
                Caso B: Usuário quer selecionar um projeto pre-existente
                '''
                # Lista os projetos disponíveis
                print('Escolha pelo o índice o projeto desejado. Projetos disponíveis:')
                projects = ctrl._list_folders(folder_name = 'projects')
                print(projects)
                index = int(input("Índice do projeto (número): "))

                if projects:
                    project_selected = projects[index]
                    print("Projeto selecionado: ", project_selected)
        else:
            print('Número não disponível no menu')

        # TODO: CONTINUAR AQUI A CRIACAO DE TRAIN, TESTE E VALIDACAO
        # 1. instanciar o projeto - OK
        # 2. uma vez instanciado o projeto, escolha 
        #   treinar
        #   testar
        #   validar
        # 3. colocar no controller a chamada para essas tres funcoes.
        
        ctrl.set_project(folder_name = project_selected)

        display_project_menu()

        # TODO: CONFERIR ESTRUTURA COM O PROFESSOR


        # # CASO A. Treinar um modelo:
        # name_train = 'treino_epoch_100' # nome do treino dado pelo usuario. Por exemplo, treino_epoch_100
        # input_file_train = '' # arquivo de entrada para treino
        # ctrl.train_model(name_train, input_file_train)

        # # B. Testar um modelo:
        # ctrl.train_model(name_train, input_file_train)

        # # C. Usar um modelo para fazer um predict:
        # ctrl.train_model(name_train, input_file_train)


if __name__ == '__main__':
    """
    Caso 1: Usuário quer criar um novo projeto
        Simula a entrada de dados do usuário para criar um novo projeto.
    """
    choice_create = 1 # Simula a escolha do modelo 01 do menu, criação de projeto
    name_project = 'Classificação de Itens'# nome do projeto
    description = 'Classificação de imagens segundo quantidade de itens' # descrição do projeto
    model = 0 # Simula a escolha do modelo 01 do menu, criação de projeto

    with patch('builtins.input', side_effect=[choice_create,name_project,description,model]):
         main()
    
    """
    Caso 2: Usuário quer selecionar um projeto
        Simula a entrada de dados do usuário para criar um novo projeto.
    """
    choice_select = 2 # Simula a escolha do modelo 02 do menu, seleção de projeto
    project_select = 0 # Simula a escolha do projeto 1

    with patch('builtins.input', side_effect=[choice_select,0]):
         main()