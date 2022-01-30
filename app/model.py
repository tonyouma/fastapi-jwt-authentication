from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)
    class Config:
        schema_extra = {
            "post-demo": {
                "title": "some title",
                "content": "some content",
            }
        }


class userSchema(BaseModel):
    # id: int = Field(default=None)
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        the_schema = {
            "user-demo": {
                "name": "Bek",
                "email": "help@bektest.com",
                "password": "123",
            }
        }

class userLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        the_schema = {
            "user-demo": {
                "email": "help@bektest.com",
                "password": "123",
            }
        }