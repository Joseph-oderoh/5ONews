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
        self.new_article = Article('Michelle Watson and Eliza Mackintosh, CNN','Pelosi makes unannounced trip to Kyiv, becoming highest-ranking US official to meet with Zelensky since the war began - CNN','House Speaker Nancy Pelosi made an unannounced trip to the Ukrainian capital on Saturday, becoming the most senior United States official to meet with President Volodymyr Zelensky since the war broke out more than two months ago','https://www.cnn.com/2022/05/01/politics/pelosi-zelensky-kyiv-ukraine-intl/index.html','https://cdn.cnn.com/cnnnext/dam/assets/220501015904-zelensky-pelosi-kyiv-050122-super-tease.jpg','2022-05-01T11:43:00Z', 'en')

    def test_instance(self):
        '''
        Test to check creation of new article instance
        '''
        self.assertTrue(isinstance(self.new_article,Article))
