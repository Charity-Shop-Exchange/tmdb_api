
from flask import Flask, render_template, redirect
import main

# Create an instance of Flask
app = Flask(__name__)

@app.route("/")
def home():

    movie_data = main.api_connect()
    # Return template and data
    return render_template("index.html", movie_data=movie_data)


if __name__ == "__main__":
    app.run(debug=True)
