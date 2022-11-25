from flask import Flask

app = Flask(__name__)

import backend.views
from backend.models.users import UserModel
from backend.models.categories import CategoryModel
from backend.models.records import RecordModel