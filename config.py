class BaseConfig:

    DEBUG = True
    TESTING = False
    SECRET_KEY = 'melhor isso aqui depois =D'


class Producao(BaseConfig):

    SECRET_KEY = 'aqui deve ser melhorado ainda mais - de um arquivo de fora.'
    DEBUG = False


class Desenvolvimento(BaseConfig):

    TESTING = True
