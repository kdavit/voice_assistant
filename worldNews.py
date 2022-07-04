import requests


def world_news(text):
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey

    # our api key
    api_key = "86207fc558fa48a19385c17e42e09785"

    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": api_key,
    }
    main_url = " https://newsapi.org/v1/articles"

    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    results = []

    for i in range(len(article) - 5):
        results.append(article[i]["title"])

    print('Results of ' + text)

    return results;
