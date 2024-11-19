import pandas as pd
import numpy as np
from pathlib import Path

class ProjectController():
    
    def __init__(self, model, view):
        '''
        Initializes a new instance of the ProjectController class.
        
        Parameters:
        -----------
    
        '''

        self._model = model
        self._view = view 


    @staticmethod
    def chose_project():
        '''
        Select the model
        '''
        pass

    def list_all_project(self) -> None:
        projects = self._model.get_project_folders()
        if not projects:
            print('Não há projetos disponíveis.')
        else:
            print('Foram encontrados os seguintes projetos:')
            for project in projects:
                print('-->', project)

    def _get_math_models(self) -> list[str]:
        models = self._model._path / 'models'
        if not models.exists():
            return []
        
        return [f.name for f in models.iterdir() if f.is_dir()]
    
    def list_math_models(self) -> None:
        all_models = self._get_math_models()

        if not all_models:
            print("Não há modelos disponíveis.")
            return None

        print("Modelos cadastrados:")
        for i, model in enumerate(all_models):
            print(f"{i} --> {model}")

        
    def manage_project_creation(self, name_project: str, description_project: str, model_project: int) -> None:
        self._model.create_project(name_project, description_project, model_project)

    def manage_train_model(self, model: str) -> None:
        model.train()

    def manage_train_model(self, model: str) -> None:
        model.test()

    def manage_predict_model(self, model: str) -> None:
        model.test()

    def delete_project(self, name_project: str) -> None:
        pass

if __name__ == '__main__':
    ctrl = ProjectController()
    ctrl.list_all_project()
    ctrl.create_new_project("nome_projeto", 'description_project', 'keras')
    print('End')