# flask-movie-api
Rest API server with CRUD based routes using Python and MongoDB, and tested using Postman

# Movie API

This is a simple Flask-based RESTful API for managing movie data in a MongoDB database.

## Prerequisites

- Python 3.x
- Flask
- pymongo

## Getting Started

1. Clone the repository: https://github.com/your-username/movie-api.git

2. Install the required dependencies: pip install -r requirements.txt
 
3. Make sure you have MongoDB installed and running on your local machine.

4. Update the MongoDB connection URL in the code:

```python
client = MongoClient("mongodb://localhost:27017/")
```

## Run the application
```python app.py```

The API will be accessible at http://localhost:5000.

## Getting Started
GET /movies
Retrieve a list of all movies.

GET /movies/<name>
Retrieve details of a specific movie by its name.

POST /movies
Create a new movie by providing the movie data in the request body.

PUT /movies/<id>
Update an existing movie by its ID. Provide the updated movie data in the request body.

DELETE /movies/<id>
Delete a movie by its ID.



   

