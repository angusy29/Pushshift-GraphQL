from graphene import ObjectType, List, String, Int, Boolean
import json
from schema import Post
from rest_api import get_submissions
from utils import json2obj

class GraphQueryLangApi(ObjectType):
    submissions = List(Post,
                        q=String(required=False),
                        size=Int(required=False),
                        sort=String(required=False),
                        sort_type=String(required=False),
                        author=String(required=False),
                        subreddit=String(required=False))

    def resolve_submissions(self, info, **kwargs):
        '''
        Resolves subreddit_submissions query
        Resolvers must return a Python object, so we serialize our reponse
        into JSON, and then deserialize into objects
        :param info:
        :param args:    Variadic arguments
        :return:
        '''
        response = get_submissions(kwargs)
        return json2obj(json.dumps(response.json['data']))