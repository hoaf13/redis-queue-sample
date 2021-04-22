from flask import Flask, render_template, url_for, redirect
import os
import redis 
from rq import Queue

app = Flask(__name__)
r = redis.Redis()
q = Queue(connection=r)

app.config.from_object('config')

from app.mod_pages.controllers import mod_pages as pages_module
from app.api.controllers import api as api_module

app.register_blueprint(pages_module)
app.register_blueprint(api_module)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')