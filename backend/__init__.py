##app = Flask(__name__)

from backend.app import create_app

app = create_app()


import backend.jwt
#from backend.jwt import create_jwt

#create_jwt(app)

#import backend.jwt