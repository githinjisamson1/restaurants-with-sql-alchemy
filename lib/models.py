#!/usr/bin/env python3

from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()


class Restaurant(Base):
    # name
    __tablename__ = "restaurants"

    # columns
    restaurant_id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())

    # representation
    def __repr__(self):
        return f'Restaurant(restaurant_id={self.restaurant_id}, ' + \
            f'name={self.name}, ' + \
            f'price={self.price})'


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    def __repr__(self):
        return f'Customer(customer_id={self.customer_id}, ' + \
            f'first_name={self.first_name}, ' + \
            f'last_name={self.last_name})'


class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer(), primary_key=True)
    restaurant_id = Column(Integer(), ForeignKey("restaurants.restaurant_id"))
    customer_id = Column(Integer(), ForeignKey("customers.customer_id"))
