from flask import Flask

from blog.conf import config
from blog.conf.export import db


class AppBuilder:

    def __init__(self):
        self.app = Flask(config.Config.APP_NAME)

    def config_app(self):
        self.app.config.from_object(config.Config)
        db.init_app(self.app)

        return self.app

    def get_app(self):
        return self.app
