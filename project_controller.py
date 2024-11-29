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
        Inicializa uma nova instancia do controlador de projetos.
        
        Parameters:
        -----------
    
        '''
        self._project = None
        self._path = Path('.') 

    def _get_folder_from_index(self, index: int, folder_name: str) -> str:
        '''
        Retorna o nome da pasta com base no índice fornecido para um foldername específico
        '''
        path_folder = self._path / folder_name
        folders = sorted([folder for folder in path_folder.iterdir() if folder.is_dir()])
        if index < 0 or index >= len(folders):
            print(f"Error: indice '{index}' não existe")
            return None
        return folders[index].name
        
    def _get_next_prefix(self, folder_name) -> str:
        '''
        Define o prefixo para a próxima pasta a ser criada
        '''
        projects_path = self._path / f'{folder_name}'
        return sum(1 for folder in projects_path.iterdir() if folder.is_dir())
    
    def _list_folders(self, folder_name: str) -> list[str]:
        '''
        Lista as pastas dentro de uma pasta específica
        '''
        path = self._path / folder_name
        if not path.exists():
            return []
        return [f.name for f in path.iterdir() if f.is_dir()]
    
    def _create_readme(self, project_path: Path, name_project: str, description: str, model: str) -> None:
        '''
        Cria o readme inicial deste projeto
        '''
        with open(project_path / 'README.md', 'w', encoding='utf-8') as f:
            f.write(f"# {name_project}\n")
            f.write(f"# Descrição: {description}\n")
            f.write(f"# Modelo selecionado: {model}\n")
    
    def create_project(self, 
                       name_project: str, 
                       description: str, 
                       model: str) -> None:
        '''
        Cria um novo projeto na pasta 'projects' com base em um modelo já existente registrado em models_ia.
        '''
        
        # 1. Cria a pasta em projects
        project_prefix = self._get_next_prefix('projects')
        project_folder_name = f"{project_prefix}-{name_project}-model-{model}"
        project_path = self._path/ 'projects' / project_folder_name

        if project_path.exists():
            ##TODO: aperfeicoar identificacao de nomes duplicados
            print(f"Erro: já existe um projeto com este nome:' {project_folder_name}'")
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
        '''
        Selececiona o projeto a partir de uma lista de projetos já criados na pasta 'projects'
        '''
        projects = ctrl._list_folders(folder_name = 'projects')
        return projects[number_selection]
    
    
    def set_project(self, folder_name: str) -> None:
        '''
        Define o atributo _project com base no nome da pasta do projeto e instancia o modelo associado.
        '''
        try:
            id, rest = folder_name.split("-", 1)
            project_name, model_info = rest.rsplit("-model-", 1)
        except ValueError:
            raise ValueError(f"Projeto '{folder_name}' não segue o formato esperado.")
        
        model_path = self._get_folder_from_index(int(model_info), 'models_ia')
        if not model_path:
            raise FileNotFoundError(f"O modelo {model_path}' não está mais disponível")
        
        self._project = Project(name=project_name, 
                                project_path=folder_name,
                                description='', 
                                model=model_path) # TODO: instanciar o modelo


    def get_project(self):
        '''
        Retorna o atributo _project
        '''
        return self._project
    
    # TODO: implementar
    def train_model(self, name_train, input_file : str) -> None:
        '''
        Cria uma pasta com o nome do treino (por exemplo, 'train-1')

        '''
        #  cria a pasta com o nome do treino dentro da pasta do projeto
        idx = self._get_next_prefix(f'projects/{self._project.project_path}') -1
        folder = f'projects/{self._project.project_path}/{name_train}-train-{idx}'
        os.makedirs(folder, exist_ok=True)
        
        # promove o treino efetivo do modelo
        self._project.model.train(input_file)

        # salva o modelo treinado na pasta do treino
        self._project.model.save(folder)

        print(f"Treino {name_train} efetuado com sucesso.")

    # TODO: implementar
    def test_model(self, input_file : str) -> None:
        '''
        Testa um modelo
        '''
        self._project.model.teste()

        print(f"Teste efetuado com sucesso.")

    # TODO: implementar
    def predict_model(self, input_file : str) -> None:
        '''
        Usa um modelo selecionado para fazer uma predição
        '''
        self._project.model.predict(input_file)

        print(f"Predict efetuado com sucesso.")



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

    # instancia a classe
    ctrl = ProjectController()

    # parametros
    name_prj = 'nome_projeto_teste'
    description_prj =  'Descricao do Projeto de Teste'
    num_model_prj = 0

    # criacao do projeto
    created_project_folder = ctrl.create_project(name_prj, description_prj, 0)

    # deleta projeto recém criado
    print('Deletando o projeto recem criado...')
    # shutil.rmtree(ctrl._path / 'projects' / created_project_folder)	