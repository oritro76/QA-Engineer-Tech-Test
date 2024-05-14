from typing import List, Dict, Optional

from random_data.random_data import RandomData


class PostsData:
    def __init__(self, num_of_posts: int = 100) -> None:
        self.posts: List[Dict] = RandomData().create_random_posts(num_of_posts)

    def get_all_posts(self) -> List[Dict]:
        return self.posts

    def get_post_by_id(self, post_id: int) -> Optional[Dict]:
        try:
            return next(post for post in self.posts if post["id"] == post_id)
        except StopIteration:
            return None

    def add_post(self, post: Dict) -> Optional[Dict]:
        new_post: Dict = {"id": len(self.posts) + 1}
        if "userId" in post and "title" in post and "body" in post:
            new_post.update(post)  # Update with user-provided data
            self.posts.append(new_post)
            return new_post
        return None

    def update_post(self, post_id: int, updated_post: Dict) -> Optional[Dict]:
        try:
            post_index = next(
                index for index, post in enumerate(self.posts) if post["id"] == post_id
            )
            self.posts[post_index] = {
                "id": post_id,
                "title": updated_post.get("title", self.posts[post_index].get("title")),
                "body": updated_post.get("body", self.posts[post_index].get("body")),
            }
            return self.posts[post_index]
        except StopIteration:
            return None

    def delete_post(self, post_id: int) -> bool:
        try:
            post_index = next(
                index for index, post in enumerate(self.posts) if post["id"] == post_id
            )
            del self.posts[post_index]
            return True
        except StopIteration:
            return False