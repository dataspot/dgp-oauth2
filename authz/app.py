from flask import Flask
from flask.ext.cors import CORS
from .blueprints import datastore


# Create application
app = Flask('service', static_folder=None)

# CORS support
CORS(app)

# Register bluprints
app.register_blueprint(datastore.blueprint, url_prefix='/datastore')