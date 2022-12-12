# BackEnd Laboratory Works

## Tasks

You can see the task for each laboratory work in their own README.md:

[Laboratory Work 1 Task](https://github.com/IvanOmelchenkoIP/BackEnd-Labs/blob/main/docs/lab-1/README.md)
[Laboratory Work 2 Task](https://github.com/IvanOmelchenkoIP/BackEnd-Labs/blob/main/docs/lab-2/README.md)
[Laboratory Work 3 Task](https://github.com/IvanOmelchenkoIP/BackEnd-Labs/blob/main/docs/lab-3/README.md)

## Local Launch

**Make sure that you have [Python](https://www.python.org/downloads/) installed (program was written in Python 3.10.5)**

Clone git repository:

    git clone https://github.com/IvanOmelchenkoIP/BackEnd-Labs.git

Create virtual environment:

*For Windows:*

    py -3 -m venv env

*For Linux:*

    python3 -m venv env

Launch virtual environment:

*For Windows:*

    .\env\scripts\activate

*For Linux:*

    source ./env/bin/activate

Install dependencies:

    pip install -r requirements.txt

Deactivate virtual environment:

    deactivate

Set FLASK_APP variable:

*For Windows:*

    set FLASK_APP=backend

*For Linux:*

    export FLASK_APP=backend

Launch virtual environment again (described before). Run the app:

    flask run –host 0.0.0.0 -p 5005

### Dockerfile

To run Dockerfile use following commands:

    docker-compose build
    docker-compose up

### Launch of Laboratoy Work 3

Local and Dockerfile Launch of Lab 3 slightly differ from previous labs, as this lab requires JWT_SECRET_KEY. Additional data is describes in [Laboratory Work 3 README](https://github.com/IvanOmelchenkoIP/BackEnd-Labs/blob/main/docs/lab-3/README.md) 

## Testing

Endpoints testing each individual lab is described is their respective README.md:

[Testing Laboratory Work 1](https://github.com/IvanOmelchenkoIP/BackEnd-Labs/blob/main/docs/lab-1/README.md)

[Testing Laboratory Work 2](https://github.com/IvanOmelchenkoIP/BackEnd-Labs/blob/main/docs/lab-2/README.md)

[Testing Laboratory Work 3](https://github.com/IvanOmelchenkoIP/BackEnd-Labs/blob/main/docs/lab-3/README.md)

## Deployment

### Heroku

[App on Heroku](https://backend-laboratory-works.herokuapp.com/) - index page shows NotFound, but response will be shown upon using any of the paths described earlier

#### Process

The app named backend-laboratory-works was created on Heroku and then deployed using GitHub Actions (*see ./github/workflows/heroku-deploy.yml*)

### Render

[App on Render](https://backend-labs.onrender.com/) - index page shows NotFound, but response will be shown upon using any of the paths described earlier

#### Process

The app was deployed on [render.com](https://render.com/) by creating a Web Service with the following parameters:

![render-deploy](https://github.com/IvanOmelchenkoIP/BackEnd-Labs/blob/main/readme/render-deploy.png)

The app uses [Free Web Service](https://render.com/docs/free) program