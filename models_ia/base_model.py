from abc import ABC, abstractmethod

class BaseModel(ABC):
    """
        Inicializa uma instância da classe BaseModel com os parâmetros especificados.
        
        Args:
            model_name (str): Nome do modelo.
            model_type (str): Tipo do modelo.
            model_path (str): Caminho para salvar/carregar o modelo.
            model_params (dict): Parâmetros de inicialização do modelo.
        """

    def __init__(self, model_name, model_type, model_path, model_params):
        pass

    @abstractmethod
    def train(self, train_params):
        pass

    @abstractmethod
    def test(self, test_params):
        pass

    @abstractmethod
    def predict(self, predict_params):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass