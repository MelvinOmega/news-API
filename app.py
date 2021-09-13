# from flask import Flask, render_template
# from newsapi import NewsApiClient


# app = Flask(__name__)



# @app.route('/')
# def Index():
    # newsapi = NewsApiClient(api_key="58b6623b42d44eef9aae1e4cb150dba2")
    # topheadlines = newsapi.get_top_headlines(q='bitcoin',
    #                                       sources='bbc-news,the-verge',
    #                                       category='business',
    #                                       language='en',
    #                                       country='ke')

# /v2/everything
    # all_articles = newsapi.get_everything(q='bitcoin',
    #                                   sources='bbc-news,the-verge',
    #                                   domains='bbc.co.ke,techcrunch.com',
    #                                   from_param='2017-12-01',
    #                                   to='2017-12-12',
    #                                   language='en',
    #                                   sort_by='relevancy',
    #                                   page=2)  

# /v2/top-headlines/sources
    # sources = newsapi.get_sources() 


#     newsapi = NewsApiClient(api_key="58b6623b42d44eef9aae1e4cb150dba2")
#     topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")


#     articles = topheadlines['articles']

#     desc = []
#     news = []
#     img = []


#     for i in range(len(articles)):
#         myarticles=[articles[i]]

#         news.append(myarticles['title'])
#         desc.append(myarticles['description'])
#         img.append(myarticles['urlToImages'])

#     mylist = zip(news, desc, img)



#     return render_template('index.html', context= mylist)



# if __name__ == "__main__":
#     app.run(debug=True)