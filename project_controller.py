from pathlib import Path
import sys
import os

# Adiciona a pasta raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from model.project import Project

import shutil

class ProjectController():
    
    def __init__(self):
        '''
        Initializes a new instance of the ProjectController class.
        
        Parameters:
        -----------
    
        '''
        self.project = None
        self._path = Path('.') 

    def _get_folder_from_index(self, index: int, folder_name: str) -> str:
        models_path = self._path / folder_name # ex: folder_name = 'models_ia'
        folders = sorted([folder for folder in models_path.iterdir() if folder.is_dir()])
        if index < 0 or index >= len(folders):
            print(f"Error: indice 'f{index}' não existe")
            return None
        return folders[index].name
        
    def _get_next_prefix(self, folder_name) -> str:
        projects_path = self._path / f'{folder_name}'
        return sum(1 for folder in projects_path.iterdir() if folder.is_dir())
    
    def _list_folders(self, folder_name: str) -> list[str]:
        path = self._path / folder_name
        if not path.exists():
            return []
        return [f.name for f in path.iterdir() if f.is_dir()]
    
    def _create_readme(self, project_path: Path, name_project: str, description: str, model: str) -> None:
        with open(project_path / 'README.md', 'w', encoding='utf-8') as f:
            f.write(f"# {name_project}\n")
            f.write(f"# Descrição: {description}\n")
            f.write(f"# Modelo selecionado: {model}\n")
    
    def create_project(self, 
                       name_project: str, 
                       description: str, 
                       model: str) -> None:
        
        # 1. Cria a pasta em projects
        project_prefix = self._get_next_prefix('projects')
        project_folder_name = f"{project_prefix}-{name_project}-model-{model}"
        project_path = self._path/ 'projects' / project_folder_name

        if project_path.exists():
            ##TODO: aperfeicoar identificacao de nomes duplicados
            print(f"Erro: já existe um projeto com este nome:' {name_project}'")
            return
        project_path.mkdir(parents=True, exist_ok=True)

        # 2. Cria um readme padrão dentro da pasta do projeto:
        self._create_readme(project_path, name_project, description, model)
    
        # 3. Gerencia a copia de arquivos do modelo para a pasta do projeto
        model_folder = self._get_folder_from_index(model, 'models_ia')
        json_path = self._path / 'models_ia' / model_folder / "hyperparameters.json"
        try:
            shutil.copy(json_path, project_path)
        except PermissionError as e:
            print(f"Erro de permissão ao acessar o arquivo ou pasta: {e}")
            return None
        except Exception as e:
            print(f"Erro: {e}")

        # Final do processo
        print(f"O projeto '{project_folder_name}' com modelo {model} foi criado.")

        return project_folder_name

    def select_project(self, number_selection: int) -> None:
        projects = ctrl._list_folders(folder_name = 'projects')
        return projects[number_selection]
    
    
    def get_instanciate_project(self, folder_name: str) -> None:
        try:
            id, rest = folder_name.split("-", 1)
            project_name, model_info = rest.rsplit("-model-", 1)
        except ValueError:
            raise ValueError(f"Projeto '{folder_name}' não segue o formato esperado.")
        
        self._get_folder_from_index(int(id), folder_name)

        # Procura o modelo correspondente na pasta models_ia
        model_path = find_model_by_number(models_folder, model_number)
        if not model_path:
            raise FileNotFoundError(f"Modelo correspondente a 'model-{model_number}' não encontrado na pasta '{models_folder}'.")

        # Cria e retorna a instância do projeto
        return Project(name=project_name, model_path=model_path)


        self.project = Project()

    # @staticmethod
    # def chose_project():
    #     '''
    #     Select the model
    #     '''
    #     pass

    # def list_all_project(self) -> None:
    #     projects = self._model.get_project_folders()
    #     if not projects:
    #         print('Não há projetos disponíveis.')
    #     else:
    #         print('Foram encontrados os seguintes projetos:')
    #         for project in projects:
    #             print('-->', project)

    # def _get_math_models(self) -> list[str]:
    #     models = self._model._path / 'models'
    #     if not models.exists():
    #         return []
        
    #     return [f.name for f in models.iterdir() if f.is_dir()]
    
    # def list_math_models(self) -> None:
    #     all_models = self._get_math_models()

    #     if not all_models:
    #         print("Não há modelos disponíveis.")
    #         return None

    #     print("Modelos cadastrados:")
    #     for i, model in enumerate(all_models):
    #         print(f"{i} --> {model}")


    # def manage_train_model(self, model: str) -> None:
    #     model.train()

    # def manage_train_model(self, model: str) -> None:
    #     model.test()

    # def manage_predict_model(self, model: str) -> None:
    #     model.predict()

    # def delete_project(self, name_project: str) -> None:
    #     pass

if __name__ == '__main__':
    ctrl = ProjectController()
    ctrl.create_project("nome_projeto_teste", 'Descricao do Projeto Teste', 1)
    print('End')