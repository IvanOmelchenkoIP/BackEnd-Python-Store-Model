# Old Deployment

## Heroku

[App on Heroku](https://backend-laboratory-works.herokuapp.com/) - index page shows NotFound, but response will be shown upon using any of the paths described earlier

### Process

The app named backend-laboratory-works was created on Heroku and then deployed using GitHub Actions (*see ./github/workflows/heroku-deploy.yml*)

## Render

[App on Render](https://backend-labs.onrender.com/) - index page shows NotFound, but response will be shown upon using any of the paths described earlier

### Process

The app was deployed on [render.com](https://render.com/) by creating a Web Service with the following parameters:

![render-deploy](https://github.com/IvanOmelchenkoIP/BackEnd-Labs/blob/main/docs/old_deploy/files/render-deploy.png)

The app uses [Free Web Service](https://render.com/docs/free) program

#### V.3.0.0

V.3.0.0 was deployed on [render.com](https://render.com/). Link to the [V.3.0.0 App](https://backend-lab-3.onrender.com/)

##### Process

The process is the same as for previous render deployment, but JWT_SECRET_KEY was also set in the settings of the web service:

- Generation of the key in python console of my device:

![jwt_generation](https://github.com/IvanOmelchenkoIP/BackEnd-Python-Store-Model/blob/main/docs/old_deploy/files/jwt_generation.png)

- Setting JWT_SECRET_KEY environment variable:

![jwt_set](https://github.com/IvanOmelchenkoIP/BackEnd-Python-Store-Model/blob/main/docs/old_deploy/files/jwt_set.png)