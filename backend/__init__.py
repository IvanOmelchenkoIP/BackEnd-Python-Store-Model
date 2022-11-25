from flask import Flask

app = Flask(__name__)

from backend.models.records import RecordModel
from backend.models.categories import CategoryModel
from backend.models.users import UserModel

import backend.views