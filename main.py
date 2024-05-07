from flask import Flask

from views import root_app
from views import cat_app


app = Flask(__name__)

app.register_blueprint(root_app)
app.register_blueprint(cat_app)





