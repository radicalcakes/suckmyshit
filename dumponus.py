import os
import datetime
import ast
import redis
from flask import (Flask, request, url_for, json, jsonify, 
                                render_template, redirect)
from flask.ext.uploads import (UploadSet, configure_uploads, 
                                                    IMAGES, UploadNotAllowed, patch_request_class)
import config
from PIL import Image
from werkzeug import secure_filename
from pyhashxx import hashxx
import models


app = Flask(__name__)

#config object, load oduction from envvar
app.config.from_object(config)

db = redis.StrictRedis(db=0)

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

# 32 mb max upload size
patch_request_class(app, 32 * 1024 * 1024)

#boiler plate json response
RESP_DICT = {'data': [], 'status': 404}
resp = app.response_class(mimetype='application/json')


def return404():
    #this does not overwrite global vars
    resp.data = json.dumps(RESP_DICT)
    resp.status_code = 404
    return resp


def return400():
    #this does not overwrite global vars
    RESP_DICT['status'] = 400
    RESP_DICT['data'] = ['Invalid request!']
    resp.data = json.dumps(RESP_DICT)
    resp.status_code = 400
    return resp


def return_get_resp(images):
    """ Returns the proper response for a GET to /api/images """
    if len(images) > 0:
        RESP_DICT['data'] = images
        RESP_DICT['status'] = 200
        resp.data = json.dumps(RESP_DICT)
        resp.status_code = 200
        return resp
    else:
        return return404()


def get_content_type(ext, file):
    #returns the content type if no content type specified
    accepted_types = ['image/png', 'image/jpeg', 'image/gif', 'image/svg+xml', 'image/svg']
    mime = file.mimetype
    if mime in accepted_types:
        return mime
    else:
        contents = {'png': 'image/png', 'jpg': 'image/jpeg', 'jpeg': 'image/jpeg', 'gif': 'image/gif', 'svg': 'image/svg+xml'}
        return contents[ext]


def make_thumbnail(stream):
    #creates a thumbnail from a stream
    return


def make_hash_name(ext, name):
    #makes the hashed name to be used as the id
    i = hashxx(name) + datetime.datetime.now() + ext
    return i


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/api/images/<img_id>', methods=['GET'])
def get_image(img_id):
    img = db.get(img_id)
    if img:
        img_json = json.dumps(ast.literal_eval(img))
        resp.data = img_json
        resp.status_code = 200
        return resp
    else:
        return return404()


@app.route('/api/images', methods=['GET', 'POST'])
def get_imgs_or_post():
    images = db.lrange('data', 0, -1)
    req = request.method
    if req == 'GET':
        return return_get_resp(images)
    elif request.method == 'POST':
        file = request.files['image']
        name = secure_filename(file.filename)
        if file and photos.file_allowed(file, name):
            extension = name.split('.')[1]
            try:
                filename = photos.save(request.files['image'])
            except UploadNotAllowed:
                return return400()
            else:
                content_type = get_content_type(extension)
                return return400()
    else:
        return return400()


if __name__ == '__main__':
    app.run()
