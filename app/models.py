class Source:
    '''
    Source class to define source objects
    '''
    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        
class Headlines:
    '''
    Class that instantiates objects of the headlines categories objects of the news sources
    '''
    def __init__(self,author,title,description,publishedAt,url,image):
        self.author = author
        self.title = title   
        self.description = description
        self.url = url
        self.image = image     
        self.publishedAt = publishedAt
class Article:
    '''
    Class that instantiates objects of the news article objects of the news sources
    '''
    def __init__(self,author,description,publishedAt,url,urlToImage,title):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
      
        