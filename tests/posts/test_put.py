import pytest
from requests.exceptions import RequestException
from requests import codes as https_status_codes
from apis.json_placeholder_posts import Posts

class TestPutPosts:
    posts = Posts()
    
    @pytest.mark.smoke
    def test_update_post_success(self, random_post_body, random_post_title, use_mock_server):
        """Test that PUT /posts/:id updates a post"""
        post_id = self.posts.get_random_post_id()
        post_body = random_post_body
        post_title = random_post_title

        update_data = {"title": post_title, "body": post_body}
        updated_post = self.posts.update_post(post_id, update_data)

        assert isinstance(updated_post, dict)
        assert updated_post["id"] == post_id
        assert updated_post["body"] == post_body
        assert updated_post["title"] == post_title

    def test_update_post_non_existent_id(self, random_post_title):
        """Test that PUT /posts/:id returns 404 for non-existent ID"""
        non_existent_id = 12345
        with pytest.raises(RequestException) as excinfo:
            self.posts.update_post(non_existent_id, {"title": random_post_title})
        assert excinfo.value.response.status_code == https_status_codes.not_found
