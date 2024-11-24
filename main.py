from project_model import ProjectModel
from view import ProjectView
from project_controller import ProjectController

    
def main():
    prj = ProjectModel()
    view = ProjectView()
    ctrl = ProjectController()

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
                    ### O projeto é criado como uma nova pasta no diretório 'projects' com o nome do projeto.
                    ### Como eu ligo um projeto a um modelo matemático?
                    ### O modelo deve ser um pickle ou similar que foi treinado para este projeto e ...
                    ### ... deverá entar ter salvo as informações de treinamento e teste que foram realizados? Como? Json tb?
                    
                    ### TODO:
                    # CRIAR PASTA, QUE REPRESENTA O PROJETO NO DIRETÓRIO 'projects'
                    # COPIAR OS HYPERPARAMETROS DO MODELO MATEMATICO PARA O PROJETO
                    # DEFINIR BASE DE DADOS PARA O PROJETO 
                    # sabemos que nao tem modelo treinado que pq pasta train está vazia (obs: logs de acuracia do modelo)
                    # na pasta de teste:
                          # 
                
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