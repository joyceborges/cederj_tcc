from abc import ABC, abstractmethod

class BaseModel(ABC):
    '''
    Base class for all models
    '''

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