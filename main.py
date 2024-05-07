from flask import Flask

from views import root_app
from views import cat_app
from models import db

from flask_migrate import Migrate


app = Flask(__name__)

app.register_blueprint(root_app)
app.register_blueprint(cat_app)

app.config(
    SQLALCHEMY_DATABASE_URI="",
    SECRET_KEY="",
)

db.init_app(app=app)
migrate = Migrate(app=app, db=db)







