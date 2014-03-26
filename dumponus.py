import os
import flask
from flask.ext.sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)

#load from a config object
app.config.from_object(__name__)

#config object, load production from envvar
app.config.from_object('config')

db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run()