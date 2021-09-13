import os

class Config:
    '''
    General configuration parent class
    '''
    # NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_BASE_URL ='https://newsapi.org/v1/articles?source={}&apiKey={}'

    NEWS_API_KEY='a6c5c1049c834e5c81000fc6a5bddebc'
    CAT_API_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
    SECRET_KEY = 'MelvinOmega'
  




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}