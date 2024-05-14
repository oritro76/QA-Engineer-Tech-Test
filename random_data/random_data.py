from faker import Faker
from random import randint

class RandomData:
    fake = Faker()

    def random_post_data(self) -> dict:
        """Generates random data for a new post."""

        return {
            "title": self.random_post_title(),
            "body": self.random_post_body(),
            "userId": 1,
        }


    def random_post_title(self) -> str:
        return self.fake.sentence()


    def random_post_body(self) -> str:
        return self.fake.paragraph()

    def create_random_posts(self, count=100) -> dict:
        posts = []
        for id in range(1, count+1):
            posts.append({
                "title": self.random_post_title(),
                "body": self.random_post_body(),
                "userId": randint(1, count + 1),
                "id": id
            })
        return posts
