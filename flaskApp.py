from flask import Flask
from flask import Response

# Definig an object for flask app
flask_app = Flask('flaskapp')

# Defining a route for the indexView
@flask_app.route('/')

# Defining the function that reflects the view response
def indexView():
    return Response(
        'Hello from the Flask app!\n',
        mimetype='text/plain'
    )

# Creating an actual flask app
app = flask_app.wsgi_app
