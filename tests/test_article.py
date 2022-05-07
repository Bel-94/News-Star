import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("ABC news", "Pauline", "Is Covid-19 Real?", "All you need to know about covid-19", "newsurl", "image", "20/04/2022")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

        

