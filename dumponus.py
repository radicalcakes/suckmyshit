import os
import ast
import redis
from flask import (Flask, request, url_for, json, jsonify, 
                                render_template, redirect)
from flask.ext.uploads import (UploadSet, configure_uploads, 
                                                    IMAGES, UploadNotAllowed, patch_request_class)

import config
from PIL import Image

app = Flask(__name__)

#config object, load oduction from envvar
app.config.from_object(config)

db = redis.StrictRedis(db=0)

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

# 32 mb max upload size
patch_request_class(app, 32 * 1024 * 1024)


def return404():
    resp_dict = {'data': [], 'status': 404}
    resp = app.response_class(mimetype='application/json')
    resp.data = json.dumps(resp_dict)
    resp.status_code = 404
    return resp

def return_get_resp(images):
    """ Returns the proper response for a GET to /api/images """
    resp_dict = {'data': [], 'status': 404}
    resp = app.response_class(mimetype='application/json')
    if len(images) > 0:
        resp_dict['data'] = images
        resp_dict['status'] = 200
        resp.data = json.dumps(resp_dict)
        resp.status_code = 200
        return resp
    else:
        resp = return404()
        return resp


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/api/images/<img_id>', methods=['GET'])
def get_image(img_id):
    img = db.get(img_id)
    resp = app.response_class(mimetype='application/json')
    if img:
        img_json = json.dumps(ast.literal_eval(img))
        resp.data = img_json
        return resp
    else:
        resp = return404()
        return resp


@app.route('/api/images', methods=['GET', 'POST'])
def get_imgs_or_post():
    images = db.lrange('data', 0, -1)
    req = request.method
    if req == 'GET':
        return return_get_resp(images)
    elif request.method == 'POST':
        print request.files
        # print request.values.keys()
        try: 
            filename = photos.save(request.files['image'])        
            print filename
        except UploadNotAllowed:
            print "whatever"
    else:
        return


if __name__ == '__main__':
    app.run()