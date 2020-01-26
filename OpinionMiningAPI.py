import search
import sentiment
import logging
import coloredlogs
import news
from flask import Flask, jsonify
import os

coloredlogs.install('DEBUG')

# Path to Natural Language Creds
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "natural_language_creds.json"

app = Flask(__name__)


# Get RESTful API call
@app.route('/Hackathon/<lang>/<lat>/<long>/<rad>/<name>', methods=['GET'])
def get_opinion(lang, lat, long, rad, name):
    search.work(str(lang), str(lat) + ',' + str(long) + ',' + str(int(rad)) + 'mi')
    news.getNews(name)
    opinion = sentiment.run_sentiment_analysis('tweets.txt')
    opinion += sentiment.run_sentiment_analysis('news.txt')

    # Check for + or - in front of opinion
    if opinion > 0:
        opinion = "+" + str(opinion)
    elif opinion < 0:
        opinion = str(opinion)
    else:
        opinion = str(opinion)

    # Make dictionary for send
    senti = [
        {
            'Language': lang,
            'Latitude': lat,
            'Longitude': long,
            'Radius': rad,
            'Opinion': opinion
        }
    ]

    logging.info("Opinion of city is: " + opinion)
    return jsonify(senti)


if __name__ == '__main__':
    app.run(debug=True)
