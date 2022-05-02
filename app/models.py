class Article:
    '''
    Class that instantiates objects of the news article objects of the news sources
    '''
    def __init__(self,author,description,publishedAt,url,urlToImage,title, language):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = urlToImage
        self.publishedAt = publishedAt
        self.language = language
class Source:
    '''
    Source class to define source objects
    '''
    def __init__(self,id,name,description,url, language):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.language = language        
        
class Headlines:
    '''
    Class that instantiates objects of the headlines categories objects of the news sources
    '''
    def __init__(self,author,title,description,publishedAt,url,image, language):
        self.author = author
        self.title = title   
        self.description = description
        self.url = url
        self.image = image     
        self.publishedAt = publishedAt
        self.language = language