import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("ABC", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "url_visitfor more")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))