from flask import Flask

from backend.models.users import UserModel
from backend.models.categories import CategoryModel
from backend.models.records import RecordModel

app = Flask(__name__)

import backend.views
