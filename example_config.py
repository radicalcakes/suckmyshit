import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI =  'dialect+driver://username:password@host:port/database'
DATABASE=os.path.join(app.root_path, 'flaskr.db')
DEBUG=True
SECRET_KEY='secretkeyhere'
USERNAME='test'
PASSWORD='test'