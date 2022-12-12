# BackEnd Labratory Work 2

## Task

- Add data validation
- Add error handling
- Add ORM models
- Add functionality by variant

### Functionality By Variant:

Group number - IP-04

04 mod 3 = 1

**Variant 1.** Add currency

#### Currency:

- Add Currency entity
- Default currency can be added for every user
- When creating a record, a currency can be set, but it is not mandatory
- If a record was not set when creating a record, a default currency of a user will be used

#### Resulting Data Structure Used In Solution:

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

## Testing

To test the program you must use [Postman](https://www.postman.com/)

### Edpoints

Creating new currency (*required - currency_name*):

    /currency

Creating new user (*required - user_name, user_currency*):

    /user

Updating user default currency (*required - user_currency*):

    /user/<user_id_value>

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