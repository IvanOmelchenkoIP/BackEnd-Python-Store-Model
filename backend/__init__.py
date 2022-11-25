from flask import Flask

app = Flask(__name__)

from backend.models.users import UserModel
from backend.models.categories import CategoryModel
from backend.models.records import RecordModel

import backend.views