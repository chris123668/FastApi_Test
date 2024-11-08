# To run the API, use: uvicorn app.main:app --reload
from fastapi import FastAPI
from . import models
from .database import engine
from . routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

#models.Base.metadata.create_all(bind=engine)


# Initialize a FastAPI app instance
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# routers allow use to split large file into smaller ones 
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)



# Define a root endpoint that returns a welcome message
@app.get("/")
# Using async here is optional since FastAPI will handle async automatically.
async def root():
    return {"message": "Welcome to my API"}



