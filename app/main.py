from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

## this creates tables IF NOT EXIST ! based on models.py.
## If alembic set up, there is no use for that 
# models.Base.metadata.create_all(bind=engine)

# start app from project root folder with: uvicorn app.main:app --reload
app = FastAPI()


# allow cross domain connection (otherwise requests from the same domain only are accepted)
# it is good security practice to have the domains defined specifically
# origins = ["https://www.google.com"]

# public setting
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# fetch paths from routers folder
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Welcome to my API!"}