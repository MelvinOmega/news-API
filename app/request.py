import urllib.request
import json
from .models import Sources, Articles
from datetime import datetime

# Getting api key
api_key = None

# Getting the news base url
base_url = None

# Getting the articlces url
articles_url = None


def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)
    print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
     
    return sources_results


def process_sources(sources_list):
    '''
    Function that processes the news sources results and turns them into a list of objects
    Args:
            sources_list: A list of dictionaries that contain sources details
    Returns:
            sources_results: A list of sources objects
    '''
    sources_results = []

    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        sources_object = Sources(
            id, name, description, url, category, country, language)
        sources_results.append(sources_object)

    return sources_results


def get_articles(id):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    get_articles_url = articles_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_results = json.loads(url.read())

        articles_object = None
        if articles_results['articles']:
            articles_object = process_articles(articles_results['articles'])

    return articles_object


def process_articles(articles_list):
    '''
    '''
    articles_object = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')

        if image:
            articles_result = Articles(
                id, author, title, description, url, image, date)
            articles_object.append(articles_result)

    return articles_object








# from app import app
# import urllib.request,json
# from .models import news

# News= news.News


# # Getting api key
# api_key = app.config['NEWS_API_KEY']

# # Getting the movie base url
# base_url = app.config["NEWS_API_BASE_URL"]


# def get_news(category):
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_news_url = base_url.format(category,api_key)

#     with urllib.request.urlopen(get_news_url) as url:
#         get_news_data = url.read()
#         get_news_response = json.loads(get_news_data)

#         news_results = None

#         if get_news_response['results']:
#             news_results_list = get_news_response['results']
#             news_results = process_results(news_results_list)



# def process_results(news_list):
#     '''
#     Function  that processes the movie result and transform them to a list of Objects

#     Args:
#         news_list: A list of dictionaries that contain movi details

#     Returns :
#         news_results: A list of movie objects
#     '''
#     movie_results = []
#     for news_item in news_list:
#         id = news_item.get('id')
#         title = news_item.get('original_title')
#         overview = news_item.get('overview')
#         poster = news_item.get('poster_path')
#         vote_average = news_item.get('vote_average')
#         vote_count = news_item.get('vote_count')

#         if poster:
#             news_object = News(id,title,overview,poster,vote_average,vote_count)
#             news_results.append(news_object)

#     return news_results



# Getting api key
# api_key = app.config['NEWS_API_KEY']



# import urllib.request,json
# from .models import Article, Category, Source , Headlines

# # Getting api key
# api_key = None
# # Getting source url
# source_url= None
# # Getting source url
# cat_url= None

# def configure_request(app):
#     global api_key, source_url, cat_url
#     api_key = app.config['NEWS_API_KEY']
#     source_url= app.config['NEWS_API_SOURCE_URL']
#     cat_url=app.config['CAT_API_URL']


# def get_source():
#     '''
#     Function that gets the json response to url request
#     '''
#     get_source_url= source_url.format(api_key)
#     # print(get_source_url)
#     with urllib.request.urlopen(get_source_url) as url:
#         get_sources_data = url.read()
#         get_sources_response = json.loads(get_sources_data)

#         source_results = None

#         if get_sources_response['sources']:
#             source_results_list = get_sources_response['sources']
#             source_results = process_results(source_results_list)

#     return source_results

# def process_results(source_list):
#     '''
#     function to process results and transform them to a list of objects
#     Args:
#         source_list:dictionary cotaining source details
#     Returns:
#         source_results: A list of source objects
#     '''
#     source_results = []
#     for source_item in source_list:
#         id = source_item.get('id')
#         name = source_item.get('name')
#         description = source_item.get('description')
#         url = source_item.get('url')
#         if id:
#             source_object = Source(id,name,description,url)
#             source_results.append(source_object)

#     return source_results

# def article_source(id):
#     article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
#     print(article_source_url)
#     with urllib.request.urlopen(article_source_url) as url:
#         article_source_data = url.read()
#         article_source_response = json.loads(article_source_data)

#         article_source_results = None

#         if article_source_response['articles']:
#             article_source_list = article_source_response['articles']
#             article_source_results = process_articles_results(article_source_list)


#     return article_source_results

# def process_articles_results(news):
#     '''
#     function that processes the json files of articles from the api key
#     '''
#     article_source_results = []
#     for article in news:
#         author = article.get('author')
#         description = article.get('description')
#         time = article.get('publishedAt')
#         url = article.get('urlToImage')
#         image = article.get('url')
#         title = article.get ('title')

#         if url:
#             article_objects = Article(author,description,time,image,url,title)
#             article_source_results.append(article_objects)

#     return article_source_results

# def get_category(cat_name):
#     '''
#     function that gets the response to the category json
#     '''
#     get_category_url = cat_url.format(cat_name,api_key)
#     print(get_category_url)
#     with urllib.request.urlopen(get_category_url) as url:
#         get_category_data = url.read()
#         get_cartegory_response = json.loads(get_category_data)

#         get_cartegory_results = None

#         if get_cartegory_response['articles']:
#             get_cartegory_list = get_cartegory_response['articles']
#             get_cartegory_results = process_articles_results(get_cartegory_list)

#     return get_cartegory_results

# def get_headlines():
#     '''
#     function that gets the response to the category json
#     '''
#     get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
#     print(get_headlines_url)
#     with urllib.request.urlopen(get_headlines_url) as url:
#         get_headlines_data = url.read()
#         get_headlines_response = json.loads(get_headlines_data)

#         get_headlines_results = None

#         if get_headlines_response['articles']:
#             get_headlines_list = get_headlines_response['articles']
#             get_headlines_results = process_articles_results(get_headlines_list)

#     return get_headlines_results