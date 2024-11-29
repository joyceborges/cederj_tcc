from pathlib import Path

class Project():
    
    def __init__(self, name = None, project_path= None, description = None, model=None, name_model=None):
        '''    
        Inicializa uma nova instância da classe Project.

        Parâmetros:
        -----------
        name : str
            O nome do projeto.

        description : str
            Uma breve descrição do projeto

        model : Model
            Uma instância da classe Model, representando o modelo a ser utilizado 
            com suas configurações específicas.

        model_name : str
            O nome do modelo a ser utilizado
        '''

        self.name = name
        self.project_path = project_path
        self.description = description
        self.model = model