
<img src="https://cdn.discordapp.com/attachments/670826877715218442/671005755574583299/Drawing_4.jpeg" width="500">


------------------------
Made with the Django Hackathon Starter Repo [here](https://github.com/DrkSephy/django-hackathon-starter)


Table of Contents
-----------------

- [Features](#features)
- [What It Does](#what-it-does)
- [Inspiration](#inspiration)
- [What We Learned](#what-we-learned)
- [Pre-requisites](#pre-requisites)
- [Getting Started](#getting-started)
- [Obtaining API Keys](#getting-api-keys)
- [What's Next](#whats-next)


Features
--------
1. Obtains the tweets and news (Twitter API and NewsAPI)
2. Calculate the happiness index of the media (Google Cloud NLP Sentiment Analysis)
3. Map the data (Leaflet.js, MapBox)
4. Render maps in a website. (Django, JS)
5. Provide supplemental information on a given place with economic data and facial emotions from local images (Quandl, Microsoft Cognitive Services API)


<hr>


What It Does
-----------------

For each place on the map, we take a sample of recent tweets and news from the location and determine how positive or negative people are at the moment. We use this information to generate a happiness index and color the map accordingly.

How is this different from a general "happiness score"? It's kind of like weather and climate — traditional happiness scores are the long-term climate of a place, whereas our approach measures the emotional weather in real time, allowing companies and governments to see how their policies and programs affect an area over time.

<hr>


Inspiration
-----------------

Americans are the unhappiest they've been in years (according to the World Happiness Report). Addressing this problem requires data analysis and action.

Mapping happiness will make the world happier. Here's why: companies and governments act based on the information they have, so access to our maps would incentivize the promotion of happiness in the same way demographic and economic maps prompt companies to launch targeted marketing campaigns and governments to pursue economic equality.

<hr>


What We Learned
-----------------

In addition to learning about the frameworks and languages we used, we started learning about the applications of this technology:

1. For airlines, monitoring happiness levels close to airports could encourage first-time flyers to travel by showing that they are not as unhappy as they might expect
2. For governments, a happiness heat map could help effect targeted policy change that helps the people who need it most, addressing economic and social inequality from an emotional perspective.
3. For companies using targeted advertisement, this data is needed to generate marketing campaigns based on the emotions of a place.

The happiness heat map is potentially a software with commercial application that could be modified to the use cases of different companies. In addition, we can make the data public through a general demo site, where the public and governments can see how a place is doing and what areas might need policy changes.

<hr>


Pre-requisites
--------------

This project relies on `bower` for front-end dependencies, which in turn requires [npm](https://www.npmjs.com/). `npm` is now bundled with `NodeJS`, which you can download and install [here](https://nodejs.org/download/).

For Python-specific libraries, this project relies on [pip](https://pypi.python.org/pypi/pip). The easiest way to install `pip` can be [found here](https://pip.pypa.io/en/latest/installing.html).


Getting Started
---------------
To get up and running, simply do the following:

    $ git clone https://github.com/anthony-zhou/tamuhack-project
    $ cd tamuhack-project

    # Install the requirements
    $ pip install -r requirements.txt
    $ pip3 install -r requirements.txt

    # Install bower
    $ npm install -g bower
    $ bower install

    # Perform database migrations
    $ python manage.py makemigrations
    $ python manage.py migrate
    
    # Start the API
    $ python3 OpinionMiningAPI.py 
    
    # Open a new terminal, navigate to hackathon_starter directory
    $ python manage.py runserver
    

<hr>

Getting API Keys
----------------

<img src="https://sejalseecharam.files.wordpress.com/2018/03/twitter-round-logo-png-transparent-background-7.png" width="200">

1. Register an account on [Twitter.com](http://www.twitter.com/)
2. Visit the [Yelp for developers page](https://developer.twitter.com/en/apply-for-access)
3. You will obtain the following: `CONSUMER KEY`, `CONSUMER SECRET`, `ACCESS_KEY`, `ACCESS_SECRET`
4. Fill in this information in search.py

<hr>

<img src="https://newsapi.org/images/n-logo-border.png" width="200">

1. Register an account on [NewsApi.org](http://www.NewsApi.org/)
2. Get your API keys and apply then in the approp
3. Add your API keys in the appropriate place in news.py

<hr>

<img src="https://www.searchpng.com/wp-content/uploads/2019/02/Google-Cloud-Logo-PNG-Image-715x715.png" width="200">  

1. Follow the quickstart for [Natural Language API](https://cloud.google.com/natural-language/docs/quickstart)
2. After you obtain your credentials you will want to place the json file in your project folder.
3. Add environment variables, either in your IDE or on your OS. For Windows it is 
```
    $ set GOOGLE_APPLICATION_CREDENTIALS=<PATH-TO-JSON>.json
   
    # On Linux it is
    $ export GOOGLE_APPLICATION_CREDENTIALS=<PATH-TO-JSON>.json
```

<hr>

<img src="https://upload.wikimedia.org/wikipedia/en/2/26/Quandl-logo.png" width="150">

1. Register an account on [Quandl.com](https://www.quandl.com/).
2. Get API Key
3. Apply the API key to appropriate place in code

<hr>

<img src="https://msdnshared.blob.core.windows.net/media/2017/03/Azure-Cognitive-Services-e1489079006258.png" width="200">

1. Register an account on [Microsoft Cognitive Services](https://azure.microsoft.com/en-us/try/cognitive-services/)
2. Get API key for https://azure.microsoft.com/en-us/try/cognitive-services/ision and for Faces
3. Follow instructions

<hr>

<img src="https://logos-download.com/wp-content/uploads/2016/02/Bing-logo.png" width="250">

1. Open [Bing Images](https://www.bing.com/images).
2. Search for the particular area you're analyzing and download pictures for Microsoft Cognitive Services to apply sentiment analysis

<hr>

<img src="https://cdn-images-1.medium.com/fit/t/1600/480/1*NfVUM4Y3im00smTtxY4sZQ.png" width="300">

1. Open [OpenCageData.com](https://opencagedata.com/) for geolocation.
2. Create and account and acquire API key.
3. Attach it in OpinionMiningAPI.py in line 22

What's Next?
----------------

1. Fully automate choropleth map generation
2. Map emotions other than happiness
3. Consider business applications

