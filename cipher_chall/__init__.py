import os
from flask import Flask

from cipher_chall import pages

def create_app():
	app = Flask(__name__)
	
	app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'dev-key-placeholder')

	app.register_blueprint(pages.bp)
	return app
