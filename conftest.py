import pytest
from faker import Faker


@pytest.fixture
def faker():
    fake = Faker()
    return fake