from flask_sqlalchemy import SQLAlchemy
from flask import Flask, app
from flask_migrate import Migrate

db=SQLAlchemy()

def create_app():
    app=Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://sample2:Sa_123456@localhost/voxgen'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app)
    migrate = Migrate(app,db)

    # app.register_blueprint(views, url_prefix='/')
    # app.register_blueprint(quest, url_prefix='/')

    return app
