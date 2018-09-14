from collections import namedtuple
import json
import requests


def get_request(url):
    '''
    Makes GET request to url
    :param url: url
    :return: response
    '''
    response = requests.get(url)
    response.raise_for_status()
    return response

def build_url(url, kwargs):
    url += f'?size={str(kwargs.get("size", 25))}'
    url += f'&sort={kwargs.get("sort", "desc")}'
    url += f'&sort_type={kwargs.get("sort_type", "created_utc")}'

    if kwargs.get('q'):
        url += f'&q={kwargs.get("q")}'

    if kwargs.get('author'):
        url += f'&author={kwargs.get("author")}'

    if kwargs.get('subreddit'):
        url += f'&subreddit={kwargs.get("subreddit")}'

    return url

def build_elastic_url(url, kwargs):
    # Example URL
    # https://elasticsearch.pushshift.io/?q="Carrie Fisher" AND score:>100&sort=created_utc:desc&size=100
    queries = []

    if kwargs.get("q"):
        pass

    if kwargs.get("title"):
        queries.append(f'title:{kwargs.get("title")}')

    if kwargs.get("score"):
        pass

    if kwargs.get("num_comments"):
        pass

    if kwargs.get("author"):
        queries.append(f'author:{kwargs.get("author")}')

    if kwargs.get("subreddit"):
        queries.append(f'subreddit:{kwargs.get("subreddit")}')

    if kwargs.get("over_18"):
        queries.append(f'over_18:{kwargs.get("over_18")}')

    for idx, query in enumerate(queries):
        if idx == 0:
            url += '?q='
        url += f'{query}'
        if idx is not len(queries) - 1:
            url += ' OR '

    url += f'&sort={kwargs.get("sort_type", "created_utc")}:{kwargs.get("sort", "desc")}'
    url += f'&size={str(kwargs.get("size", 25))}'

    return url


def _json_object_hook(d):
    keys = []
    # this is for handling elasticsearch responses with keys prefixing _
    for key in d.keys():
        keys.append(key[1:]) if key[0] == '_' else keys.append(key)

    return namedtuple('DataRow', keys)(*d.values())


def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)
