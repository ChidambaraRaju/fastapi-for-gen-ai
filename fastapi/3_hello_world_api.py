# Import the FastAPI class from the fastapi module
from fastapi import FastAPI

# Create an instance of the FastAPI class
# This instance will be our main application where we define routes/endpoints
app = FastAPI()

# Define a route for the root URL ("/") using the GET method
# When someone accesses the root URL, this function will be executed
@app.get("/")
def hello():
    # Return a JSON response with a message
    return {"message": "Hello world!"}

# Define another route for the URL "/about" using the GET method
# When someone accesses "/about", this function will be executed
@app.get("/about")
def about():
    # Return a JSON response with a different message
    return {"message": "This is my first api"}
