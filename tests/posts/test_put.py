from apis.json_placeholder_posts import get_all_posts, update_post
import pytest
from requests.exceptions import RequestException
from requests import codes as https_status_codes

def test_update_post_success():
    """Test that PUT /posts/:id updates a post"""
    posts = get_all_posts()
    post_id = posts[0]["id"]
    update_data = {"title": "Updated Title"}
    updated_post = update_post(post_id, update_data)
    assert isinstance(updated_post, dict)
    assert updated_post["id"] == post_id



def test_update_post_non_existent_id():
    """Test that PUT /posts/:id returns 404 for non-existent ID"""
    non_existent_id = 12345
    with pytest.raises(RequestException) as excinfo:
        update_post(non_existent_id, {"title": "New Title"})
    assert excinfo.value.response.status_code == https_status_codes.not_found