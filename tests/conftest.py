"""Defines fixtures available to all tests."""
import pytest

from app.app import create_app
from app.settings import TestingConfig


@pytest.fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_app(TestingConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture()
def client(app):
    return app.test_client()


