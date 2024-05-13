from random_data.random_data import RandomData


class PostsData:
    def __init__(self, num_of_posts=100):
        self.posts = RandomData().create_random_posts(num_of_posts)

    def get_all_posts(self):
        return self.posts

    def get_post_by_id(self, post_id):
        try:
            return next(post for post in self.posts if post["id"] == post_id)
        except StopIteration:
            return None

    def add_post(self, new_post):
        new_post["id"] = len(self.posts) + 1
        self.posts.append(new_post)
        return new_post

    def update_post(self, post_id, updated_post):
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

    def delete_post(self, post_id):
        try:
            post_index = next(
                index for index, post in enumerate(self.posts) if post["id"] == post_id
            )
            del self.posts[post_index]
            return True
        except StopIteration:
            return False
