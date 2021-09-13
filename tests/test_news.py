import unittest
from app.models import news


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = news('BBC','World Drowning','url','The world is drowning slowly','content of the article','link','date')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,news))

if __name__ == '__main__':
    unittest.main()
