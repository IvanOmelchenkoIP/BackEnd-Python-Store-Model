# BackEnd Labratory Work 1

## Task

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

## Testing

To test the program you must use [Postman](https://www.postman.com/)

### Endpointss

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