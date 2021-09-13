class News:
    """
    News class for News
    """

    def __init__(self,author,title,urlToImage,description,content,url,publishedAt):
            self.author = author
            self.title = title
            self.urlToImage =urlToImage
            self.description = description
            self.content = content
            self.url = url
            self.publishedAt = publishedAt
        
class  Sources:
            """
            Sources class to define the sources objects
            """
            def __init__(self,id,name,description,url,category,language,country):
                    self.id = id
                    self.name = name
                    self.description = description
                    self.url = url
                    self.category = category
                    self.language = language
                    self.country = country



# class Article:
#     '''
#     Class that instantiates objects of the news article objects of the news sources
#     '''
#     def __init__(self,author,description,time,url,image,title):
#         self.author = author
#         self.description = description
#         self.time = time
#         self.url = url
#         self.image = image
#         self.title = title

# class Category:
#     '''
#     Class that instantiates objects of the news categories objects of the news sources
#     '''
#     def __init__(self,author,description,time,url,image,title):
#         self.author = author
#         self.description = description
#         self.time = time
#         self.url = url
#         self.image = image
#         self.title = title

# class Source:
#     '''
#     Source class to define source objects
#     '''
#     def __init__(self,id,name,description,url):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.url = url

# class Headlines:
#     '''
#     Class that instantiates objects of the headlines categories objects of the news sources
#     '''
#     def __init__(self,author,description,time,url,image,title):
#         self.author = author
#         self.description = description
#         self.time = time
#         self.url = url
#         self.image = image
#         self.title = title

