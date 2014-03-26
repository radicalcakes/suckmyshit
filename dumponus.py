import os
import flask
from flask.ext.sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)

#load from a config object
app.config.from_object(__name__)

#config object, load production from envvar
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='suckmyshit53454%',
    USERNAME='radicalcakes',
    PASSWORD='Tr@p3z01d',
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Tr@p3z01d@localhost/dumponus'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)


if __name__ == '__main__':
    app.run()