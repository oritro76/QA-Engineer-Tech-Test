import pytest
from faker import Faker

@pytest.fixture
def random_post_data():
  """Generates random data for a new post."""

  faker = Faker()
  return {
      "title": faker.sentence(),
      "body": faker.paragraph(),
      "userId": 1,  # Replace with a valid user ID if needed
  }