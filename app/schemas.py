from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Annotated, Optional
from pydantic.types import conint


# Define a Post model using Pydantic's BaseModel to enforce the data structure.
# This model defines the fields that are required for a post object in the API.

class PostBase(BaseModel):
    title: str  # Title of the post (string)
    content: str  # Content of the post (string)
    published: bool = True 


class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

# This class is the response of what we will send to the user
#we only want to send back what is important to them 
class Post(PostBase):
    id: int
    created_at: datetime
    user_id: int
    owner: UserOut

# this class tell pydantic to ignore that the post is not in a dict format
# b/c were using sqlachemly
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(strict=True, le=1)]
    