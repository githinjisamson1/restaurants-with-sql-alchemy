
# Restaurants With SQLAlchemy

We have three models: `Restaurant`, `Review`, and `Customer`.
For our purposes, a Restaurant  has many `Review`s, a `Customer` has many `Review`s, and a `Review` belongs to a `Restaurant` and to a `Customer`. `Restaurant` - `Customer` is a many-to-many relationship.

## Authors

- [@githinjisamson1](https://www.github.com/githinjisamson1)


## Contributing

Contributions are always welcome!




## Features

Object Relationship Methods
Use SQLAlchemy query methods where appropriate.
Review
- `Review customer()`
  - should return the `Customer` instance for this review
- `Review restaurant()`
  - should return the `Restaurant` instance for this review
 

Restaurant
- `Restaurant reviews()`
  - returns a collection of all the reviews for the `Restaurant`
- `Restaurant customers()`
  - returns a collection of all the customers who reviewed the `Restaurant`
 

Customer
- `Customer reviews()`
  - should return a collection of all the reviews that the `Customer` has left
- `Customer restaurants()`
  - should return a collection of all the restaurants that the `Customer` has reviewed
 

You can create a `debug.py` file and use it to check that these methods work before proceeding.
For example, you should be able to call `session.query(Customer).first().restaurants` and see a list of the restaurants for the first customer in the database based on your seed data; and `session.query(Review).first().customer` should return the customer for the first review in the database.
 

Aggregate and Relationship Methods
Customer
- `Customer full_name()`
  - returns the full name of the customer, with the first name and the last name concatenated Western style.
- `Customer favorite_restaurant()`
  - returns the restaurant instance that has the highest star rating from this customer
- `Customer add_review(restaurant, rating)`
  - takes a `restaurant` (an instance of the `Restaurant` class) and a rating creates a new review for the restaurant with the given `restaurant_id`
- `Customer delete_reviews(restaurant)`
  - takes a `restaurant` (an instance of the `Restaurant` class) and removes **all** their reviews for this restaurant
Review
- `Review full_review()`
  - should return a string formatted as follows:
        - Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.
Restaurant
- `Restaurant fanciest(), this method should be a class method`
  - returns _one_ restaurant instance for the restaurant that has the highest price
- `Restaurant all_reviews()`
  - should return a list of strings with all the reviews for this restaurant formatted as follows:
-------------------------------------------------------------------------------------------------------------------------
  "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
  "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
]

## Lessons Learned

- SQLAlchemy Migrations
- SQLAlchemy Relationships
- Class and Instance Methods
- SQLAlchemy Querying


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Used By

For Practice :)
