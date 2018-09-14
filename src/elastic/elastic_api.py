from flask import jsonify
from utils import get_request, build_elastic_url

def get_elastic_submissions(kwargs):
    '''
    Keyword arguments fed into this function, builds URL based on arguments
    Then makes a GET request to the URL
    :param kwargs:
    :return: JSON response
    '''

    # Example query
    # https://elasticsearch.pushshift.io/?q="Carrie Fisher" AND score:>100&sort=created_utc:desc&size=100

    search_subreddit_url = 'https://elastic.pushshift.io/rs/submissions/_search/'
    url = build_elastic_url(search_subreddit_url, kwargs)
    response = get_request(url)
    return jsonify(response.json())