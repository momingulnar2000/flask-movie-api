from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

#connection to a local MongoDB server
client = MongoClient("mongodb://localhost:27017/")
db = client["movies_db"]
collection = db["movies"]

#GET Route to reterive movies/data from MongoDB
@app.route("/movies")
def get_movies():
    movies = list(collection.find())
    # Convert ObjectId to string representation
    for movie in movies:
        movie["_id"] = str(movie["_id"])
    return jsonify(movies)


#GET Route to reterive specifice movie/data from MongoDB
@app.route("/movies/<name>", methods=["GET"])
def get_movie_by_name(name):
    movie = collection.find_one({"name": name})
    if movie:
        movie["_id"] = str(movie["_id"])
        return jsonify(movie)
    else:
        return jsonify({"message": "Movie not found"}), 404

#POST Route to insert/create new movie data in MongoDB
@app.route("/movies", methods=["POST"])
def create_movie():
    try:
        data = request.json
        result = collection.insert_one(data)
        inserted_id = str(result.inserted_id)
        data["_id"] = inserted_id
        return jsonify(data)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": "An error occurred while creating the movie"}), 500

#PUT Route to update existing movie in MongoDB
@app.route("/movies/<id>", methods=["PUT"])
def update_movie(id):
    data = request.json
    collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify(data)

#DELETE movie 
@app.route("/movies/<id>", methods=["DELETE"])
def delete_movie(id):
    collection.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Movie deleted"})

if __name__ == "__main__":
    app.run(debug=True)
