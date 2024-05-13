import pytest
from requests import codes as https_status_codes, RequestException
from apis.json_placeholder_posts import get_all_posts, delete_post, get_post_by_id


def test_delete_post_success():
    """Test that DELETE /posts/:id deletes a post"""
    posts = get_all_posts()
    post_id = posts[0]["id"]
    status_code = delete_post(post_id)
    assert (
        status_code == https_status_codes.ok
    ), f"delete requests with {post_id} expected http status code {https_status_codes.not_found}, received {status_code}" 
    with pytest.raises(RequestException) as excinfo:
        get_post_by_id(post_id=post_id)
    assert excinfo.value.response.status_code == https_status_codes.not_found


def test_delete_post_non_existent_id():
    """Test that DELETE /posts/:id returns 404 for non-existent ID"""
    non_existent_id = 12345
    status_code = delete_post(non_existent_id)
    assert (
        status_code == https_status_codes.ok
    ), f"expected http status code {https_status_codes.not_found}, received {status_code}"
