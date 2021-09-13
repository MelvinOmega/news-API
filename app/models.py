class Sources:
    '''
    Sources class to define Sources Objects
    '''

    def __init__(self,id,name,description,url,category,country,language):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language

class Articles:
    '''
    Articles class to define articles objects
    '''
    def __init__(self,id,author,title,description,url,image,date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date 



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

