import argparse

from model import ProjectModel
from view import ProjectView
from project_controller import ProjectController

    
def main():
    model = ProjectModel()
    view = ProjectView()
    ctrl = ProjectController(model, view)

    while True:
        try:
            ctrl._view.display_menu()

            choice = ctrl._view.get_user_choice_menu()

            if choice == 1:
                ctrl.list_all_project()
            elif choice == 2:
                ctrl.list_all_project()
                project = ctrl._view.get_user_choice_model()               
            elif choice == 3:
               # Adiciona nome
                name = input("Digite o nome do projeto: ").strip()
                # Adiciona modelo matemático
                ctrl.list_math_models()
                math_model = ctrl._view.get_user_choice_model()
                # Adiciona descrição
                description = input("Escreva a descrição do projeto: ").strip()

                if all([name, math_model, description]):
                    ctrl.manage_project_creation(name, description, math_model)
                else:
                    print("Nome e Modelos Matemático não podem estar vazios. Por favor, preencha estes campos.")
            elif choice == 4:
                ctrl.manage_train_model()
            else:
                break

        except Exception as e:
            print(f"An error occurred: {e}")
            continue

if __name__ == '__main__':
    main()
    print('End')