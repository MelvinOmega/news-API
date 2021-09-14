from flask import render_template
from . import main
from ..requests import get_sources, get_articles
from ..models import Sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    sources = get_sources('sources')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    title = "News Highlighter"
    return render_template('index.html')


@main.route('/sources/<id>')
def articles(id):
    '''
    view articles page
    '''
    articles = get_articles(id)
    title = f'NH | {id}'

    return render_template('articles.html', title=title, articles=articles)    

# from flask import render_template
# from app import app

# # Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     return render_template('index.html')

















# from flask import render_template, request, redirect, url_for
# from flask import current_app
# from .import main
# from ..requests import get_sources, get_articles
# from ..models import Sources

# # views
# @main.route('/')
# def index():
#     '''
#     view root page function that returns the index the page and its data
#     '''
#     sources = get_sources('sources')
#     sports_sources = get_sources('sports')
#     technology_sources = get_sources('technology')
#     entertainment_sources = get_sources('entertainment')
#     title = "News Highlighter"
    

#     return render_template('index.html', title=title, sources=sources, sports_sources=sports_sources, technology_sources=technology_sources, entertainment_sources=entertainment_sources)
    
    

# @main.route('/sources/<id>')
# def articles(id):
#     '''
#     view articles page
#     '''
#     articles = get_articles(id)
#     title = f'NH | {id}'

#     return render_template('articles.html', title=title, articles=articles)


# from . import main
# from flask import render_template,request,redirect,url_for
# from ..request import get_source,article_source,get_category,get_headlines
# from ..request import get_news


# #our views
# @main.route('/')
# def index():
#     '''
#     Root function returning index/home page with data
#     '''
#     source= get_source()
#     headlines = get_headlines()
#     return render_template('index.html',sources=source, headlines = headlines)

# @main.route('/article/<id>')
# def article(id):

#     '''
#     View article page function that returns the various article details page and its data
#     '''
#     # title= 'Articles'
#     articles = article_source(id)
#     return render_template('article.html',articles= articles,id=id )

# @main.route('/categories/<cat_name>')
# def category(cat_name):
#     '''
#     function to return the categories.html page and its content
#     '''
#     category = get_category(cat_name)
#     title = f'{cat_name}'
#     cat = cat_name

#     return render_template('categories.html',title = title,category = category, cat= cat_name)


