from flask import Flask

app = Flask(__name__)


from face_render import views
from face_render import error_hendler