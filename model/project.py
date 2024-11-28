from pathlib import Path

class Project():
    
    def __init__(self, name = None, description = None, model=None):
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
        self.model = model #### modelo