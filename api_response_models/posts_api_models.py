from pydantic import BaseModel, Field
from typing import List


class Post(BaseModel):
    userId: int = Field(description="ID of the user who created the post")
    id: int = Field(description="Unique identifier for the post")
    title: str = Field(description="Title of the post")
    body: str = Field(description="Body content of the post")

class PostListResponse(BaseModel):
    data: List[Post] = Field(description="List of post objects")

