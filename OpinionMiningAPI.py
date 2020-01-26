import search
import sentiment
import logging
import coloredlogs
import news
from flask import Flask, jsonify
import os
import sys

sys.path.insert(1, "/hackathon_starter/hackathon/scripts")

import images

coloredlogs.install('DEBUG')

# Path to Natural Language Creds
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "natural_language_creds.json"

app = Flask(__name__)


# Get RESTful API call
@app.route('/Hackathon/<lang>/<lat>/<long>/<rad>/<name>', methods=['GET'])
def get_opinion(lang, lat, long, rad, name):
    search.work(str(lang), str(lat) + ',' + str(long) + ',' + str(int(rad)) + 'mi')
    news.getNews(name)
    twitterOpinion = sentiment.run_sentiment_analysis('tweets.txt')
    newsOpinion = sentiment.run_sentiment_analysis('news.txt')
    visual = images.process_image_search(name)

    # Check for + or - in front of opinion
    if newsOpinion > 0:
        newsOpinion = "+" + str(newsOpinion)
    elif newsOpinion < 0:
        newsOpinion = str(newsOpinion)
    else:
        newsOpinion = str(newsOpinion)
        
    if twitterOpinion > 0:
        twitterOpinion = "+" + str(twitterOpinion)
    elif twitterOpinion < 0:
        twitterOpinion = str(twitterOpinion)
    else:
        twitterOpinion = str(twitterOpinion)

    # Make dictionary for send
    senti = [
        {
            'Language': lang,
            'Latitude': lat,
            'Longitude': long,
            'Radius': rad,
            'News Opinion': news,
            'Twitter Opinion': twitterOpinion,
            'Opinion': twitterOpinion + newsOpinion,
            'Visual' : visual
        }
    ]

    logging.info("Opinion of city is: " + twitterOpinion + newsOpinion)
    return jsonify(senti)


if __name__ == '__main__':
    app.run(debug=True)
