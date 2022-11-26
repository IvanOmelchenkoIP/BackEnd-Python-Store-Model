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

*For Windows:*_*

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

### Testing

To test the program you must use [Postman](https://www.postman.com/)

#### Laboratory Work 1

Creating new user (*required - user_name*):

    /newuser

Creating new category (*required - category_name*):

    /newcategory

Creating new record (*required - user_id, category_id, record_sum*):

    /newrecord

Getting users (was implemented for ability to keep track of user_id of created users as they are randomly generated):

    /users

Getting categories:

    /categories

Geting records:

    /records
    /records?user_id=<value>
    /records?user_id=<value>&category_id=<value>

#### Laboratory Work 2

Creating new currency (*required - currency_name*):

    /currency

Creating new user (*required - user_name, user_currency*):

    /user

Updating user default currency (*required - user_currency*):

    /user/<currency_id_value>

Creating new category (*required - category_name*):

    /category

Creating new record (*required - user_id, category_id, record_sum, not mandatory - record_currency*):

    /record

Getting currencies:

    /currency

Getting currency by id:

    /currency/<currency_id_value>

Getting users:

    /user

Getting user by id:

    /user/<user_id_value>

Getting categories:

    /category

Getting category by id:

    /category/<category_id_value>

Geting records:

    /record
    /record?user_id=<value>
    /record?user_id=<value>&category_id=<value>

Getting record by id:

    /record/<record_id_value>

## Deployment

[App on Heroku](https://backend-laboratory-works.herokuapp.com/) - index page shows NotFound, but response will be shown upon using any of the paths described earlier

### Process

The app named baackend-laboratory-works was created on Heroku and then deployed using GitHub Actions (*see ./github/workflows/heroku-deploy.yml*)
