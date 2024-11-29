from abc import ABC, abstractmethod

class DatasetModel(ABC):
    '''
    Classe responsável para garantir a entrada correta de dados para um modelo.
    '''
    
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def standardize_file(self):
        '''
        Método abstrato para padronizar os arquivos de entrada do modelo.

        Este método é responsável por aplicar as especificações de tipo e/ou formato
        nos arquivos enviados pelo usuário, padronizando as entradas de dados
        para o formato aceito pelo modelo.
        '''
        pass

    @abstractmethod
    def load_file(self):
        """
        Método abstrato para carregar um arquivo que servirá de entrada para o modelo.

        Este método tem como objetivo garantir que diferentes tipos de entradas
        possam ser acessadas para processamente e pode incluir a leitura de arquivos
        em diferentes formator, como imagens, CSV ou json.
        """
        pass