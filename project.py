import pandas as pd
import numpy as np
from pathlib import Path

class Project():
    
    def __init__(self, name, description, model):
        '''
        Initializes a new instance of the Project class.
        
        Parameters:
        -----------
        name : str
            The name of the project.
        
        description : str
            A brief description of the project's purpose, objectives, or details.
        
        model : int
            An index representing the selected model configuration, including custom hyperparameters
            and other custom settings (e.g., CPU allocation, specific parameters).
        
        '''
        self.name = name  # nome do projeto
        self.description = description  # descrição do projeto
        self.model = model  # indexador do modelo selecionado: hyperparâmetros personalizados, outros parâmetros personalizados (CPU...)

        self._operations = {"create": 'create a new project',
                             "open": 'open a new project',
                             "save": 'save a project'}

    @staticmethod
    def list_all_project() -> str:
        """
        Lists all folders inside the 'projects' directory within the specified path.
        If no path is provided, it defaults to the current working directory.

        Parameters:
        -----------
        path_folder : str, optional
            The path to the parent directory where the 'model' folder is located. Defaults to the current directory.
        
        Returns:
        --------
        str
            A string listing all the folder names inside the 'model' folder.
        """

        project_folder = Path.cwd() / 'projects'

        if not project_folder.exists():
            print('A error ocurred! The project_folder does not exist!')
            return None
        
        projects_folders = [f.name for f in project_folder.iterdir() if f.is_dir()]
        print('We founded the following projects: ')
        for project in projects_folders:
            print('-->',project)

        return projects_folders
    
    @staticmethod
    def create_new_project(name_project: str, description_project: str, model_project: int) -> None:
        '''
        Create a new project
        '''

        path = Path.cwd() / 'projects'/ name_project
        if path.exists():
            print(f"Error: There is a project with the same name '{name_project}' ")
        else:
            # Create the folder if it does not exist
            path.mkdir(exist_ok=True)
            print(f"The project '{name_project}' has been created.")


    @staticmethod
    def create_new_project(name_project: str, description_project: str, model_project: int) -> None:
        '''
        Create a new project
        '''

        path = Path.cwd() / 'projects'/ name_project
        if path.exists():
            print(f"Error: There is a project with the same name '{name_project}' ")
        else:
            # Create the folder if it does not exist
            path.mkdir(exist_ok=True)
            print(f"The project '{name_project}' has been created.")

    @staticmethod
    def chose_project():
        '''
        Select the model
        '''
        pass


if __name__ == '__main__':
    prj = Project(None, None, None)
    # prj.list_all_project()
    prj.create_new_project("nome_projeto", 'description_project', 'keras')
    print('End')