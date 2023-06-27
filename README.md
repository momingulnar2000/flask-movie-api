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
## Sample Data

The API uses the following sample data:

```json
[{
  "name": "Harry Potter and the Order of the Phoenix",
  "img": "https://bit.ly/2IcnSwz",
  "summary": "Harry Potter and Dumbledore's warning about the return of Lord Voldemort is not heeded by the wizard authorities who, in turn, look to undermine Dumbledore's authority at Hogwarts and discredit Harry."
}, {
  "name": "The Lord of the Rings: The Fellowship of the Ring",
  "img": "https://bit.ly/2tC1Lcg",
  "summary": "A young hobbit, Frodo, who has found the One Ring that belongs to the Dark Lord Sauron, begins his journey with eight companions to Mount Doom, the only place where it can be destroyed."
}, {
  "name": "Avengers: Endgame",
  "img": "https://bit.ly/2Pzczlb",
  "summary": "Adrift in space with no food or water, Tony Stark sends a message to Pepper Potts as his oxygen supply starts to dwindle. Meanwhile, the remaining Avengers -- Thor, Black Widow, Captain America, and Bruce Banner -- must figure out a way to bring back their vanquished allies for an epic showdown with Thanos -- the evil demigod who decimated the planet and the universe."
}]
```

![image](https://github.com/momingulnar2000/flask-movie-api/assets/137852145/77668ef6-cff8-4b3c-a827-7b9a26144186)


## Run the application
```python app.py```

The API will be accessible at http://localhost:5000.

## Endpoints
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





   

