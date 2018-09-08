from flask import jsonify
from utils import get_request, build_url


def get_submissions(kwargs):
    '''
    Fed keyword arguments, builds URL based on arguments
    Then makes a GET request to the URL
    :param kwargs:
    :return: JSON response
    '''
    search_subreddit_url = 'http://api.pushshift.io/reddit/search/submission/'
    url = build_url(search_subreddit_url, kwargs)
    response = get_request(url)
    return jsonify(response.json())