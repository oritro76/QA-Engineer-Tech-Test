import pytest
import random
from random_data.random_data import RandomData

random_data = RandomData()

@pytest.fixture
def random_post_data() -> dict:
  """Generates random data for a new post."""

  return {
      "title": random_data.random_post_title(),
      "body": random_data.random_post_body(),
      "userId": random.randint(1, 100)
  }

@pytest.fixture
def random_post_title() -> str:
  return random_data.random_post_title()

@pytest.fixture
def random_post_body() -> str:
  return random_data.random_post_body()