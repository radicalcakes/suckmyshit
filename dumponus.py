import os
import flask
from flask import json, jsonify, render_template
import redis
from config import AppConfig, DB

app = flask.Flask(__name__)

#config object, load production from envvar
app.config.from_object(AppConfig)

db = redis.StrictRedis(db=DB)


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/images/<img_id>', methods=['GET'])
def get_image(img_id):
    pass


@app.route('/images', methods=['GET', 'POST'])
def get_mimgs_or_post():
    pass


if __name__ == '__main__':
    app.run()