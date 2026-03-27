from flask import Flask, render_template, request
import requests

#imports a dictionary of data from dog_breeds.py and "prettifies", or styles, the dog names when they appear in the HTML page
from dog_breeds import prettify_dog_breed

# Initialize the Flask application
app = Flask(__name__)

#function adds a dash in the URL between breed names with multiple words like miniature poodle
def check_breed(breed):
  return "/".join(breed.split("-"))

@app.route("/", methods=["GET", "POST"])
def puppito_pic_gallery():
  errors = []
  breed = ""
  number = ""
  if request.method == "POST":
     breed = request.form.get("breed")
     number = request.form.get("number")
  if not breed:
     errors.append("Woof! Please choose a puppito breed")
  if not number:
     errors.append("rrruff! Select a number of pup pics please")
  if breed and number:
     response = requests.get("https://dog.ceo/api/breed/" + check_breed(breed) + "/images/random/" + number)
     data = response.json()
     puppito_pics = data["message"]
     return render_template("dogs.html", images=puppito_pics, breed=prettify_dog_breed(breed), errors=[])
  return render_template("dogs.html", images=[], breed="", errors=errors)

app.debug = True

# Run the flask server
if __name__ == "__main__":
    app.run()