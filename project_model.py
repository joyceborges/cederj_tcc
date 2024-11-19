from pathlib import Path

class ProjectModel():
    
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
        
        self._path = Path.cwd()

    def get_project_folders(self) -> list[str]:
        project_folder = self._path / 'projects'
        if not project_folder.exists():
            return []
        return [f.name for f in project_folder.iterdir() if f.is_dir()]

    def create_project(self, 
                        name_project: str, 
                        description_project: str, 
                        model_project: int) -> None:
        '''
        Create a new project:
            open a folder in the 'projects' directory with the name of the project.
        '''

        path = self._path / 'projects'/ name_project
        if path.exists():
            print(f"Error: There is a project with the same name '{name_project}' ")
        else:
            # Create the folder if it does not exist
            path.mkdir(exist_ok=True)
            print(f"The project '{name_project}' has been created.")