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
    url += f'?size=' + str(kwargs.get('size', 25))
    url += f'&sort=' + kwargs.get('sort', 'desc')
    url += f'&sort_type=' + kwargs.get('sort_type', 'created_utc')

    if kwargs.get('q'):
        url += f'&q=' + kwargs.get('q')

    if kwargs.get('author'):
        url += f'&author=' + kwargs.get('author')

    if kwargs.get('subreddit'):
        url += f'&subreddit='  + kwargs.get('subreddit')

    return url

def _json_object_hook(d):
    return namedtuple('DataRow', d.keys())(*d.values())


def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)
