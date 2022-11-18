import flask
from flask import request, jsonify, render_template

app = flask.Flask(__name__)

# Create some test data for our catalog in the form of a list of dictionaries.
movies = [
    {'id': 0,
     'title': 'The Shawsank Redemption',
     'year': '1994'},
    {'id': 1,
     'title': 'The Godfather',
     'year': '1972'},
    {'id': 2,
     'title': 'The Dark Knight',
     'year': '2008'},
    {'id': 3,
     'title': '12 Angry Men',
     'year': '1957'}
]


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


# A route to return all of the available entries in our catalog.
@app.route('/movies', methods=['GET'])
def api_all():
    return jsonify(movies)

if __name__ == "__main__":
  app.run(debug=True)

