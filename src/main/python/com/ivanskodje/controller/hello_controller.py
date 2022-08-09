from flask import Flask


class HelloController:
    app : Flask
    def __init__(self, app: Flask) -> None:
        self.app = app
    
    @app.route("/")
    def index():
        return "Hello"

