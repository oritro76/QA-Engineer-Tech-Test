from apis.json_placeholder_posts import create_post
import pytest
from requests.exceptions import RequestException
from requests import codes as https_status_codes

def test_create_post_success(random_post_data):
    """Test that POST /posts creates a new post"""
    new_post = random_post_data
    created_post = create_post(new_post)

    assert isinstance(created_post, dict)
    assert "id" in created_post


def test_create_post_empty_body():
    """Test that POST /posts with empty body returns 400"""
    with pytest.raises(RequestException) as excinfo:
        create_post({})
    assert excinfo.value.response.status_code == https_status_codes.bad_request