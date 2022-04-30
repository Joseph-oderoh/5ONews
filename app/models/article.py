class Article:
    """
    Article test  to check if properly initialized
    """
    def __init__(self,source,author,title,description,urlToImage,publishedAt):
        self.source= source
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        