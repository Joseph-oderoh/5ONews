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