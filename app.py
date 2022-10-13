#Project Flask MVC

from application import app
from flask_login import LoginManager
from flask import Flask, render_template, request




if __name__ == '__main__':
    app = Flask(__name__, template_folder="views")
    app.run(host="127.0.0.1", port=8000, debug=True)