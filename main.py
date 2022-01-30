import uvicorn
from fastapi import Body, FastAPI, Depends

# from app.model import PostSchema
from app.model import PostSchema, userSchema, userLoginSchema

from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

posts = [
    {
        "id": 1,
        "title": "penguin",
        "text": "penguin is a bird"
    },
    {
        "id": 2,
        "title": "cat",
        "text": "cat is a animal"
    },
    {
        "id": 3,
        "title": "dog",
        "text": "dog is a animal"
    }
]

users = []

from app.model import PostSchema

app = FastAPI()

@app.get("/", tags=["test"])
def greet():
    return {"message": "Hello World"}

# Get Posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data": posts}


# Get Post by ID

@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id: int):
    if id > len(posts):
        return {"error": "Post with ID is not found"}
    for post in posts:
        if post["id"] == id:
            return { "data": post}

# Post a blog post [A handler for creating a post]

@app.post("/posts", dependencies=[Depends(jwtBearer())] ,tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {"info": "Post added successfully"}

# Create a user

@app.post("/user/signup", tags=["user"])
def user_signup(user: userSchema = Body(default=None)):
    # user.id = len(users) + 1
    users.append(user)
    return signJWT(user.email)
def check_user(data: userLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@app.post("/user/login", tags=["user"])
def user_login(user: userLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    return {"error": "Invalid email or password"}

