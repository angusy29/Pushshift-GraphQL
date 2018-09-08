import pytest
import requests
from utils import get_request, build_url

class TestUtils:
    url = 'http://api.pushshift.io/reddit/search/submission/'

    def test_get_request(self):
        self.url += '?subreddit=pics'
        response = get_request(self.url)
        assert response.status_code == 200

    def test_build_url(self):
        url = build_url(self.url, {'subreddit': 'pics', 'size': 100})
        assert url == self.url + \
                           '?size=100&sort=desc&sort_type=created_utc&subreddit=pics'

        url = build_url(self.url, {'subreddit': 'oldschoolcool'})
        assert url == self.url + '?size=25&sort=desc&sort_type=created_utc&subreddit=oldschoolcool'

        url = build_url(self.url, {})
        assert url == self.url + '?size=25&sort=desc&sort_type=created_utc'