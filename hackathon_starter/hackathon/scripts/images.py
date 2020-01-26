from azure.cognitiveservices.search.imagesearch import ImageSearchClient
from msrest.authentication import CognitiveServicesCredentials
import requests
import json

SEARCH_KEY = 'e7fd0fca21264303b7d7757f3fb0d40b'
SEARCH_URL = 'https://api.cognitive.microsoft.com'
SEARCH_COUNT = 3
RECOG_KEY = '6482c5eb68a0458790882a6485213569'
RECOG_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

def process_image_search(query):
    """Search for images and return their emotional attributes."""
    # Get image search results
    client = ImageSearchClient(endpoint=SEARCH_URL, credentials=CognitiveServicesCredentials(SEARCH_KEY))
    image_results = client.images.search(query=query, count=SEARCH_COUNT)

    # Process image search results
    detected = 0
    attributes = {'anger': 0,
                  'contempt': 0,
                  'disgust': 0,
                  'fear': 0,
                  'happiness': 0,
                  'fear': 0,
                  'neutral': 0,
                  'sadness': 0,
                  'surprise': 0,
                 }
    for result in image_results.value:
        params = {'returnFaceAttributes': 'emotion', 'recognitionModel': 'recognition_02'}
        data = {'url': result.content_url}
        headers = {'Ocp-Apim-Subscription-Key': RECOG_KEY, 'Content-Type': 'application/json'}
        faces = json.loads(requests.post(RECOG_URL, params=params, json=data, headers=headers).text)
        for face in faces:
            detected += 1
            for attribute in face['faceAttributes']['emotion']:
                attributes[attribute] += face['faceAttributes']['emotion'][attribute]

    # Average attributes
    for attribute in attributes:
        attributes[attribute] /= detected

    return attributes
