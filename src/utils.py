from collections import namedtuple
import json
import requests

def get_request(url):
    '''
    Makes GET request to url
    :param url: url
    :return: json response
    '''
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def _json_object_hook(d):
    return namedtuple('DataRow', d.keys())(*d.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)
