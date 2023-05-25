from flask import Flask

app = Flask(__name__)

app.secret_key = "jgDE4ro4RtilhOrB"

from cryptocash.routes import *




