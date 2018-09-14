from graphene import ObjectType, List, String, Int, Boolean
import json
from rest.rest_schema import Post
from elastic.elastic_schema import Hits
from rest.rest_api import get_submissions
from elastic.elastic_api import get_elastic_submissions
from utils import json2obj

class GraphQueryLangApi(ObjectType):
    submissions = List(Post,
                        q=String(required=False),
                        size=Int(required=False),
                        sort=String(required=False),
                        sort_type=String(required=False),
                        author=String(required=False),
                        subreddit=String(required=False))

    elastic_submissions = List(Hits,
                               q=String(required=False),
                               title=String(required=False),
                               score=String(required=False),
                               num_comments=String(required=False),
                               over_18=String(required=False),
                               author=String(required=False),
                               subreddit=String(required=False),
                               size=Int(required=False),
                               sort=String(required=False),
                               sort_type=String(required=False))

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


    def resolve_elastic_submissions(self, info, **kwargs):
        '''
        Resolves GraphQL query for Elastic submissions
        :param info:
        :param kwargs:   Variadic arguments
        :return:
        '''
        response = get_elastic_submissions(kwargs)
        return json2obj(json.dumps(response.json['hits']['hits']))