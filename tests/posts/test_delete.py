import pytest
from requests import codes as https_status_codes, RequestException
from api_wrappers.json_placeholder_posts import Posts

class TestDeletePosts:
    post = Posts()

    @pytest.mark.smoke
    def test_delete_post_success(self, use_mock_server):
        """Test that DELETE /posts/:id deletes a post"""
        post_id = self.post.get_random_post_id()
        status_code = self.post.delete_post(post_id)
        assert (
            status_code == https_status_codes.ok
        ), f"delete requests with {post_id} expected http status code {https_status_codes.not_found}, received {status_code}" 
        
        with pytest.raises(RequestException) as excinfo:
            self.post.get_post_by_id(post_id=post_id)
        assert excinfo.value.response.status_code == https_status_codes.not_found


    def test_delete_post_non_existent_id(self):
        """Test that DELETE /posts/:id returns 404 for non-existent ID"""
        non_existent_id = 12345
        status_code = self.post.delete_post(non_existent_id)
        assert (
            status_code == https_status_codes.ok
        ), f"expected http status code {https_status_codes.not_found}, received {status_code}"
