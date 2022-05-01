class Article:
    '''
    Class that instantiates objects of the news article objects of the news sources
    '''
    def __init__(self,author,description,publishedAt,url,urlToImage,title):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = urlToImage
        self.publishedAt = publishedAt