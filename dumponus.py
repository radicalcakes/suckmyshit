import os
import redis
from flask import (Flask, request, url_for, json, jsonify, 
                                render_template, redirect)
from flask.ext.uploads import (UploadSet, configure_uploads, 
                                                    IMAGES, UploadNotAllowed, patch_request_class)
import config

app = Flask(__name__)

#config object, load production from envvar
app.config.from_object(config)

db = redis.StrictRedis(db=0)

uploaded_photos = UploadSet('photos', IMAGES)
configure_uploads(app, uploaded_photos)

#uploads of images with 32 mb max
patch_request_class(app, 32 * 1024 * 1024)


def validate_dict_fields(d):
    pass


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/api/images/<img_id>', methods=['GET'])
def get_image(img_id):
    print img_id
    print db.keys()
    img_json = json.dumps(db.get(img_id))
    if img_json:
        return app.response_class(response=img_json, mimetype='application/json')

@app.route('/api/images', methods=['GET', 'POST'])
def get_mimgs_or_post():
    pass


if __name__ == '__main__':
    app.run()