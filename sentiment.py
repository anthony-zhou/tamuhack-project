from google.cloud import language_v1
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import requests
import logging
import coloredlogs


def run_sentiment_analysis(filename):
    # Open Client
    client = language.LanguageServiceClient()

    # Open sentiment file as read only
    file = open(filename, 'r', encoding='utf-8')

    # Initialize Sentiment
    sentiment = 0

    # Traverse through text
    for line in file:
        words = str(line)

        # Call documents
        document = {
            "content": words,
            "type": enums.Document.Type.PLAIN_TEXT}

        # Attain the score of the line of text
        try:
            score = client.analyze_sentiment(document=document,
                                         encoding_type=enums.EncodingType.UTF8).document_sentiment.score
        except:
            logging.info("Big Rip on that analysis")

        if score > 0:
            sentiment += 1
        elif score < 0:
            sentiment -= 1

        # Log the Sentiment
        logging.info("Sentiment Score: " + str(score) + "--> " + words)

    # Return the value
    return sentiment


if __name__ == '__main__':
    coloredlogs.install("DEBUG")
