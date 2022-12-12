# BackEnd Labratory Work 3

## Task

- Create registration and login endpoints
- Protect other endpoints so that only logged in users have access to them
- Create testing scenario in [Insomnia](https://insomnia.rest/)

#### Data Structure Used In Solution:

Unchanged from Laboratory Work 2:

| Currency      |
| ------------- |
| id            |
| currency name |

| User        |
| ----------- |
| id          |
| user name   |
| currency id |

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
| currency id      |


## Local Launch of Lab 3

Laboratory Work 3 requires JWT_SECRET_KEY so it should be generated:

### Console Generation

First, access python terminal with the command:

    python

For generation JWT_SECRET_KEY, use commands: 

    import secrets
    secrets.SystemRandom().getRandBits(128)

**Copy the key** and exit:

    exit()

### Script Generation

Alternatively, Python Script in ./config-scripts can be launched to obtain JWT_SECRET_KEY:

    python ./config-scripts/jwt.py 

**The script should print generated key into a console, which can be copied for later use**

### Using the Generated Key

To use the copied key, set JWT_SECRET_KEY environmental variable outside of Python virtual environment:

*For Windows:*

    set JWT_SECRET_KEY=<your_key>

*For Linux:*

    export JWT_SECRET_KEY=<your_key>

Except of generating JWT_SECRET_KEY, the program can be launched like in description of all the other labs

### Dockerfile

To run Dockerfile, *first generate JWT_SECRET_KEY* as described earlier and *run docker-compose build as following:*

    docker-compose build --build-arg JWT_SECRET_KEY_VALUE=<your_key_>

Then run docker-compose:

    docker-compose up

## Testing

To test the program you must use [Insomnia](https://insomnia.rest/)

### Endpoints

Registering a user (*required - user_name, user_currency, user_password*, user will be always able to add a currency with id 1 as it is set in program to be Hryvnia):

    /register

Logging in (*required - user_name, user_password*):

    /login

Creating new currency (*required - currency_name, user has to be logged in*):

    /currency

Updating user default currency (*required - user_currency, user has to be logged in*):

    /user/<user_id_value>

Creating new category (*required - category_name, user has to be logged in*):

    /category

Creating new record (*required - user_id, category_id, record_sum, optional - record_currency, user has to be logged in*):

    /record

Getting currencies (*optional - user may be or may not be logged in*, user will be always able to get a list of currencies with initial currency with id 1 as it is set in program to be Hryvnia):

    /currency

Getting currency by id (*user has to be logged in*):

    /currency/<currency_id_value>

Getting users (*user has to be logged in*):

    /user

Getting user by id (*user has to be logged in*):

    /user/<user_id_value>

Getting categories (*user has to be logged in*):

    /category

Getting category by id (*user has to be logged in*):

    /category/<category_id_value>

Geting records (*user has to be logged in*):

    /record
    /record?user_id=<value>
    /record?user_id=<value>&category_id=<value>

Getting record by id (*user has to be logged in*):

    /record/<record_id_value>

### Storages and ORM Models

The program can work with object storages and ORM models as databases. The deployed version uses ORM models, but you can manually use test object storage. To do so, you can:

- Comment each import from the module backend.data.managers.models.managers
- Uncomment each import from the module backend.data.managers.storages.managers

This should be done in the following modules:

- Module backend.data.initial_data.currency
- Each module in package backend.endpoints.resources

If you wish to return to ORM models, revert the changes

## Deployment

The app for laboratory work 3 was deployed seperately on [render.com](https://render.com/). Link to the [Laboratory Work 3 App](https://backend-lab-3.onrender.com/)

### Testing

Loading the page may take some time. Upon opening the home page, you should see 404 error. Upon opening get requests that are not locked by jwt, you should see a response. Otherwise, you will see jwt error. [Insomnia](https://insomnia.rest/) should be used to correctly test the app.

### Process

The process is the same as for previous render deployment, but JWT_SECRET_KEY was also set in the settings of the web service:

- Generation of the key in python console of my device:

![jwt_generation](https://github.com/IvanOmelchenkoIP/BackEnd-Labs/blob/main/docs/files/jwt_generation.png)

- Setting JWT_SECRET_KEY environment variable:

![jwt_set](https://github.com/IvanOmelchenkoIP/BackEnd-Labs/blob/main/docs/files/jwt_set.png)