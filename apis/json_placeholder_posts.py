import random
from typing import List
from clients.api_client import http_api_client
from settings import BASE_URL



class Posts:
    URL = f"{BASE_URL}/posts"

    def get_all_posts(self) -> List[dict]:
        """Fetches all posts from the API and returns a list of dictionaries.

        Raises an exception for non-2xx status codes.

        Returns:
            List[dict]: A list of dictionaries representing the fetched posts.
        """
        response = http_api_client.get(self.URL)
        response.raise_for_status()
        return response.json()


    def create_post(self, data: dict) -> dict:
        """Creates a new post using the provided data and returns the response dictionary.

        Raises an exception for non-2xx status codes.

        Args:
            data (dict): Dictionary containing the post data to create.

        Returns:
            dict: The JSON dictionary representing the created post.
        """
        response = http_api_client.post(self.URL, json=data)
        response.raise_for_status()
        return response.json()


    def get_post_by_id(self, post_id: int) -> dict:
        """Fetches a post by its ID and returns the response dictionary.

        Raises an exception for non-2xx status codes.

        Args:
            post_id (int): ID of the post to fetch.

        Returns:
            dict: The JSON dictionary representing the fetched post.
        """
        url = f"{self.URL}/{post_id}"
        response = http_api_client.get(url)
        response.raise_for_status()
        return response.json()


    def update_post(self, post_id: int, data: dict) -> dict:
        """Updates a post by its ID using the provided data and returns the response dictionary.

        Raises an exception for non-2xx status codes.

        Args:
            post_id (int): ID of the post to update.
            data (dict): Dictionary containing the updated post data.

        Returns:
            dict: The JSON dictionary representing the updated post.
        """
        url = f"{self.URL}/{post_id}"
        response = http_api_client.put(url, json=data)
        response.raise_for_status()
        return response.json()


    def delete_post(self, post_id: int) -> int:
        """Deletes a post by its ID and returns the HTTP status code (optional).

        Args:
            post_id (int): ID of the post to delete.

        Returns:
            Optional[int]: The HTTP status code of the response (e.g., 204 for successful deletion),
                            or None if the API doesn't provide a status code for DELETE requests.
        """
        url = f"{self.URL}/{post_id}"
        response = http_api_client.delete(url)
        return response.status_code
    
    def get_random_post_id(self) -> int:
        """Deletes a post by its ID and returns the HTTP status code (optional).

        Args:
            post_id (int): ID of the post to delete.

        Returns:
            Optional[int]: The HTTP status code of the response (e.g., 204 for successful deletion),
                            or None if the API doesn't provide a status code for DELETE requests.
        """
        posts = self.get_all_posts()
        random_post = random.choice(posts)
        return random_post["id"]