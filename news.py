import requests


# Obtain news function
def getNews(city_name):

    # URL to obtain news from news api
    url = ('https://newsapi.org/v2/everything?'
           'apiKey=d42e88f1fb624084891e89df549c06ff&'
           'q=' + city_name + '&'
                              'language=en&'
                              'sortBy=publishedAt&'
                              'pageSize=100')

    # Get response articles
    response = requests.get(url).json()['articles']

    file = open('news.txt', 'w', encoding='utf-8')

    # Write articles to file
    for line in response:
        words = str(line['content']).replace('\n', '')
        file.write(words)
