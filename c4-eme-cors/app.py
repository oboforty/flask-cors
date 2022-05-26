import codecs
import json
import os
import time
from os.path import realpath, dirname, join
from flask import render_template, request, Response

from eme.entities import load_settings
from eme.website import WebsiteApp
from flask_cors import CORS


class HomeController():
    def __init__(self, server):
        self.group = "Home"

        server.preset_endpoints({
            'POST /api/test': 'Home:post_files',
        })

    def index(self):
        return "hello eme"

    def post_files(self):
        return json.dumps([
            {
                "id": 1,
                "asd": 53
            }
        ])


class ExampleApp(WebsiteApp):

    def __init__(self):
        # eme/examples/simple_website is the working directory.
        script_path = dirname(realpath(__file__))
        conf = load_settings(join(script_path, 'config.ini'))

        super().__init__(conf, script_path)

        self.load_controllers({
            "Home": HomeController(self)
        }, conf['routing'])


if __name__ == "__main__":
    app = ExampleApp()
    CORS(app)

    app.port = 10050
    app.host = "0.0.0.0"

    if __name__ == "__main__":
        # run it manually:
        app.start()
