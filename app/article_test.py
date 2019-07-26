import unittest
from models import article

Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test behaviour of the article class
    '''
    def setUp(self):
        '''
        Method to run before every Test
        '''
        self.new_article= Article( "sly-news","SLY News","Your trusted article for breaking news, analysis, exclusive interviews, headlines, and videos at SLYnews.com.","http://slynews.go.com","general")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,article))

if __name__ == '__main__':
    unittest.main()