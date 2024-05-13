import pytest
from requests.exceptions import RequestException
from requests import codes as https_status_codes

from apis.json_placeholder_posts import Posts, BASE_URL
from api_response_models.posts_api_models import PostListResponse, Post
from clients.api_client import http_api_client

class TestGetPosts:
    post = Posts() 

    @pytest.mark.smoke
    def test_get_all_posts(self):
        """Test that GET /posts returns a list of posts"""
        posts = self.post.get_all_posts()
        assert isinstance(posts, list)
        assert len(posts) > 0
        for post in posts:
            assert isinstance(post, dict)
            post = Post(**post)
            assert post.id, f"id is missing in for one post"
            assert post.title, f"title is missing in for post {post.id}"
            assert post.body, f"body is missing in for post {post.id}"
            assert post.userId, f"userId is missing in for post {post.id}"


    def test_get_all_posts_with_limit(self):
        """Test that GET /posts supports pagination"""
        # Test with limit of 2 posts
        post_limit=2
        response = http_api_client.get(f"{self.post.URL}?_limit={post_limit}")
        response.raise_for_status()
        data = response.json()
        assert len(data) == post_limit, f"with Limit {post_limit} expected {len(data)}"


    def test_get_all_posts_with_pagination(self):
        # Test with specific page number
        page_num = 2
        response = http_api_client.get(f"{self.post.URL}?_page={page_num}")
        response.raise_for_status()
        data = response.json()
        assert len(data) > 0, f"should have data for pagination when page_num is {page_num}"

    @pytest.mark.smoke
    def test_get_post_by_id_success(self):
        """Test that GET /posts/:id returns a post"""
        post_id = self.post.get_random_post_id()
        post = self.post.get_post_by_id(post_id)
        assert isinstance(post, dict)
        assert post["id"] == post_id, f"expected {post_id}, received {post['id']}"


    def test_get_post_by_id_not_found(self):
        """Test that GET /posts/:id returns 404 for non-existent ID"""
        non_existent_id = 12345
        with pytest.raises(RequestException) as excinfo:
            self.post.get_post_by_id(non_existent_id)
        assert excinfo.value.response.status_code == https_status_codes.not_found
