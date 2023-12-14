#!/usr/bin/env python3

from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, desc
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('sqlite:///restaurant.db')

Session = sessionmaker(bind=engine)
session = Session()


class Restaurant(Base):
    # name
    __tablename__ = "restaurants"

    # columns
    restaurant_id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())

    # relationship
    reviews = relationship("Review", back_populates="restaurant")

    # association with customers through reviews
    customers = association_proxy('reviews', 'customer',
                                  creator=lambda cu: Review(customer=cu))

    # representation
    def __repr__(self):
        return f'Restaurant(restaurant_id={self.restaurant_id}, ' + \
            f'name={self.name}, ' + \
            f'price={self.price})'

    # !OBJECT RELATIONSHIP METHODS
    def reviews(self):
        return self.reviews

    def customers(self):
        return self.customers

    # !AGGREGATE AND RELATIONSHIP METHODS
    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(desc(cls.price)).first()

    def all_reviews(self):
        review_list_comprehension = [
            item.full_review
            for item in self.reviews
        ]
        
        return review_list_comprehension


class Customer(Base):
    # name
    __tablename__ = "customers"

    # columns
    customer_id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    # relationship with Review on customer
    reviews = relationship("Review", back_populates="customer")

    # association with restaurants throught reviews
    restaurants = association_proxy('reviews', 'restaurant',
                                    creator=lambda res: Review(restaurant=res))

    # representation
    def __repr__(self):
        return f'Customer(customer_id={self.customer_id}, ' + \
            f'first_name={self.first_name}, ' + \
            f'last_name={self.last_name})'

    # !OBJECT RELATIONSHIP METHODS
    def reviews(self):
        return self.reviews

    def restaurants(self):
        return self.restaurants

    # !AGGREGATE AND RELATIONSHIP METHODS
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        # get customer first
        customer_high_rating = session.query(Review).filter_by(
            customer_id=self.customer_id).order_by(desc(Review.star_rating)).first()

        # now return the restaurant
        return customer_high_rating.restaurants

    def add_review(self, restaurant, rating):
        review = Review(restaurant, rating)
        session.add(review)
        session.commit()

    def delete_reviews(self, restaurant):
        reviews_to_delete = session.query(Review).filter_by(
            restaurant_id=restaurant.restaurant_id)

        reviews_to_delete.delete()


class Review(Base):
    # name
    __tablename__ = "reviews"

    # columns
    review_id = Column(Integer(), primary_key=True)
    restaurant_id = Column(Integer(), ForeignKey("restaurants.restaurant_id"))
    customer_id = Column(Integer(), ForeignKey("customers.customer_id"))

    # relationship with Restaurant on reviews
    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    # representation
    def __repr__(self):
        return f'Review(review_id={self.review_id}, ' + \
            f'restaurant_id={self.restaurant_id}, ' + \
            f'customer_id={self.customer_id})'

    # !OBJECT RELATIONSHIP METHODS
    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    # !AGGREGATE AND RELATIONSHIP METHODS
    def full_review(self):
        return f"Review for {self.restaurant} by {self.customer.customer()}: {self.star_rating} stars."


# !not related to the above
# TODO: understand association_proxy
'''
Notice in the Game and User models that we have added an association_proxy (imported from sqlalchemy.ext.associationproxy) to refer to the many-to-many related table. This states that there is an association through the reviews table's game or user column. The creator argument takes a function (an anonymous lambda function in this case) which accepts a game or user and returns a review for that game or user. This review has, in a sense, created the relationship between the game and user.

'''


# instances
res1 = Restaurant()
customer1 = Customer()
review1 = Review()
