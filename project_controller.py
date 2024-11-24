import pandas as pd
import numpy as np
from pathlib import Path

class ProjectController():
    
    def __init__(self):
        '''
        Initializes a new instance of the ProjectController class.
        
        Parameters:
        -----------
    
        '''
        self.project = None


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

        
    def create_project(name_project: str, description_project: str, model_project: int) -> None:
        pass

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
    ctrl.create_new_project("nome_projeto", 'description_project', 'keras')
    print('End')