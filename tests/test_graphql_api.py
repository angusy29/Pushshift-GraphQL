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


    def test_elastic_api_submission_no_arguments(self, client):
        # test no arguments
        result = self.schema.execute('{ elasticSubmissions { source { title } } }')
        assert result.errors == None
        assert len(result.data['elasticSubmissions']) == 25


    def test_elastic_api_submissions_subreddit(self, client):
        result = self.schema.execute('{ elasticSubmissions(subreddit: "pics") { source { author } } }')
        assert result.errors == None
        assert len(result.data['elasticSubmissions']) == 25

        for ordered_dict in result.data['elasticSubmissions']:
            assert 'source' in ordered_dict
            assert 'author' in ordered_dict['source']


    def test_elastic_api_submissions_size(self, client):
        result = self.schema.execute('{ elasticSubmissions(size: 5) { source { title } } }')
        assert result.errors == None
        assert len(result.data['elasticSubmissions']) == 5


    def test_elastic_api_submissions_failure(self, client):
        result = self.schema.execute('{ elasticSubmissions(subreddit: not_a_string) { source { title } }')
        assert result.errors != None