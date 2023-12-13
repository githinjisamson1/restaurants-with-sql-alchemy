#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Customer, Review

fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurant.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # empty then fill up tables upon each commence
    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.query(Review).delete()

    # actual seeding of data
    for item in range(5):
        restaurant = Restaurant(
            name=fake.unique.name(),
            price=random.randint(400, 1000)
        )
        session.add(restaurant)
        session.commit()

    for item in range(5):
        customer = Customer(
            first_name=fake.unique.name(),
            last_name=fake.unique.name(),
        )
        session.add(customer)
        session.commit()

    # we are sure data has already entered in restaurants/customers table at this point in the program
    # so we can access ids
    restaurant_ids = [item.restaurant_id for item in session.query(Restaurant)]

    customer_ids = [item.customer_id for item in session.query(Customer)]

    # similar to join table in SQL/MUST have ids from both
    for item in range(5):
        review = Review(
            restaurant_id=random.choice(restaurant_ids),
            customer_id=random.choice(customer_ids)
        )
        session.add(review)
        session.commit()

    session.close()
