import pytest
from server import create_app

@pytest.fixture
def client():
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    client = app.test_client()
    yield client
    ctx.pop()