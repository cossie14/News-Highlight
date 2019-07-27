class Article:
    '''
    Class that instantiates objects of the news article objects of the news sources
    '''
    def __init__(self,author,image,description,time,title,url):
        self.author = author
        self.image = image
        self.description = description
        self.time = time
        self.title = title
        self.url = url
      