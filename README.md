# BackEnd Store Model

## Tasks

You can see the task for each laboratory work in their own README.md:

[V.1.0.0](https://github.com/IvanOmelchenkoIP/BackEnd-Python-Store-Model/blob/main/docs/v.1.0.0/README.md)

[V.2.0.0](https://github.com/IvanOmelchenkoIP/BackEnd-Python-Store-Model/blob/main/docs/v.2.0.0/README.md)

[V.3.0.0](https://github.com/IvanOmelchenkoIP/BackEnd-Python-Store-Model/blob/main/docs/v.3.0.0/README.md)

## Local Launch

**Make sure that you have [Python](https://www.python.org/downloads/) installed (program was written in Python 3.10.5)**

Clone git repository:

    git clone https://github.com/IvanOmelchenkoIP/BackEnd-Python-Store-Model.git

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

### Launch of V.3.0.0

Local and Dockerfile V.3.0.0 slightly differ from previous labs, as this lab requires JWT_SECRET_KEY. Additional data is describes in [V.3.0.0 README](https://github.com/IvanOmelchenkoIP/BackEnd-Python-Store-Model/blob/main/docs/v.3.0.0/README.md) 

## Testing

Endpoints testing each individual lab is described is their respective README.md:

[V 1.0.0](https://github.com/IvanOmelchenkoIP/BackEnd-Python-Store-Model/blob/main/docs/v.1.0.0/README.md)

[V.2.0.0](https://github.com/IvanOmelchenkoIP/BackEnd-Python-Store-Model/blob/main/docs/v.2.0.0/README.md)

[V.3.0.0](https://github.com/IvanOmelchenkoIP/BackEnd-Python-Store-Model/blob/main/docs/v.3.0.0/README.md)

## Deployment

### Render

The app is available to test by the [link](https://backend-store-model.onrender.com)

Test via instructions in v.3.0.0

[Insomnia environment](https://github.com/IvanOmelchenkoIP/BackEnd-Python-Store-Model/blob/main/resources/insomnia_json/Insomnia_2023-01-21.json)