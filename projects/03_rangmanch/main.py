from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables
from routes.reviews import router as reviews_router


# A lifespan function runs once when FastAPI starts and once when it stops.
# @asynccontextmanager splits those two phases using `yield`.
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Everything before `yield` runs during application startup.
    # Create database tables before the app starts handling requests.
    create_tables()
    print("Database tables created")

    # `yield` tells FastAPI that startup is complete and it can serve requests.
    yield

    # Everything after `yield` runs during application shutdown.
    # Put cleanup work here, such as closing connections or stopping background tasks.
    print("Shutting down the app")

app = FastAPI(
    title= "Rangmanch Review API",
    description= "Theater Review API",
    # Tell FastAPI to use the function above for startup and shutdown tasks.
    lifespan=lifespan
)

app.include_router(reviews_router)


@app.get("/")
def root():
    return {"message": "Welcome to Rangmanch Review API"}

