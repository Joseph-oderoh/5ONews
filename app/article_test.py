import unittest
from app.models import article

Article = article.Article

class NewsTest(unittest.TestCase):
    """
      Test Class to test the behaviour of the News class
    """
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Independent','Shweta Sharma','Jack Dorsey says Twitter ‘has always tried to do its best’ ahead of $44bn sale to Elon Musk','Twitter founder attempts to address concerns after internal townhall meet amid mass exodus concerns',' "https://static.independent.co.uk/2022/04/25/17/GettyImages-1321753242.jpg?quality=75&width=1200&auto=webp','2022-04-30T08:00:00Z')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
    unittest.main()        