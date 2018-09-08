from flask import jsonify
from utils import get_request

search_subreddit_url = 'http://api.pushshift.io/reddit/search/submission/?subreddit='

def get_submissions(subreddit):
    url = search_subreddit_url + subreddit
    response = get_request(url)
    return jsonify(response)