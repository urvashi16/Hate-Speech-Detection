from flask import Flask
from app.config import Config
app = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.app_context().push()
    return app

app = create_app()
if __name__ == "__main__":
    from app.controllers import *
    from api.api import *
    app.run()