from graphene import ObjectType, List, String, Int, Boolean
import json
from schema import Post
from rest_api import get_submissions
from utils import json2obj

class GraphQueryLangApi(ObjectType):
    subreddit_submissions = List(Post, subreddit=String(required=True))

    def resolve_subreddit_submissions(self, info, **args):
        response = get_submissions(args.get("subreddit"))
        return json2obj(json.dumps(response.json["data"]))