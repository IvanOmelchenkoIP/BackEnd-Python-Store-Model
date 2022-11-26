# BackEnd Laboratory Works

## Laboratory Work 1 Task

Create REST API app about cost accounting

### Required Functionality:

- Creating new user
- Creating new category
- Creating new record
- Receiving categories list
- Receiving list of records for one user
- Receiving list of records by category of the user

### Data Structure:

| User      |
| --------- |
| id        |
| user name |

| Category      |
| ------------- |
| id            |
| category name |

| Record           |
| ---------------- |
| id               |
| user id          |
| category id      |
| date of creation |
| sum              |

## Laboratory Work 2 Task

- Add data validation
- Add error handling
- Add ORM models
- Add functionality by variant

### Functionality By Variant

Group number - IP-04

04 mod 3 = 1

**Variant 1.** Add currency

#### Currency

- Add Currency entity
- Default currency can be added for every user
- When creating a record, a currency can be set, but it is not mandatory
- If a record was not set when creating a record, a default currency of a user will be used

## Local Launch

**Make sure that you have [Python](https://www.python.org/downloads/) installed (program was written in Python 3.10.5)**

Clone git repository:

    git clone https://github.com/IvanOmelchenkoIP/BackEnd-Labs.git

Create virtual environment:

_For Windows:_

    py -3 -m venv env

_For Linux:_

    python3 -m venv env

Launch virtual environment:

_For Windows:_

    .\env\scripts\activate

_For Linux:_

    source ./env/bin/activate

Install dependencies:

    pip install -r requirements.txt

Deactivate virtual environment:

    deactivate

Set FLASK_APP variable:

_For Windows:_

    set FLASK_APP=backend

_For Linux:_

    export FLASK_APP=backend

Launch virtual environment again (described before). Run the app:

    flask run –host 0.0.0.0 -p 5005

### Dockerfile

To run Dockerfile use following commands:

    docker-compose build
    docker-compose up

### Testing

To test the program you must use [Postman](https://www.postman.com/)

Creating new user (_required - user_name_):

    /newuser

Creating new category (_required - category_name_):

    /newcategory

Creating new record (_required - user_id, category_id, record_sum_):

    /newrecord

Getting users (was implemented for ability to keep track of user_id of created users as they are randomly generated):

    /users

Getting categories:

    /categories

Geting records:

    /records
    /records?user_id=<value>
    /records?user_id=<value>&category_id=<value>

## Deployment

[App on Heroku](https://backend-laboratory-works.herokuapp.com/) - index page shows NotFound, but response will be shown upon using any of the paths described earlier

### Process

The app named baackend-laboratory-works was created on Heroku and then deployed using GitHub Actions (_see ./github/workflows/heroku-deploy.yml_)
