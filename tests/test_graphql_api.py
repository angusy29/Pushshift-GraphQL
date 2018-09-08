import graphene
from graphql_api import GraphQueryLangApi


class TestGraphQueryLangApi:
    schema = graphene.Schema(query=GraphQueryLangApi)

    def test_api(self, client):
        result = self.schema.execute('{ submissions { author } }')

        assert result.errors == None
        assert len(result.data['submissions']) == 25

        for ordered_dict in result.data['submissions']:
            assert 'author' in ordered_dict

