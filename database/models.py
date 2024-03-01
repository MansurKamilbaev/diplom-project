from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text, Float
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    phone_number = Column(Integer, unique=True)
    city = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    reg_date = Column(DateTime)


class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, unique=True)
    product_description = Column(Text)
    product_price = Column(Float)
    product_quantity = Column(Integer)


class ProductPhoto(Base):
    __tablename__ = 'product_photos'
    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    photo_path = Column(String)

    product_fk = relationship(Product, lazy='subquery')


class UserCart(Base):
    __tablename__ = 'user_carts'
    cart_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer)
    size = Column(String)
    color = Column(String)

    user_fk = relationship(User, lazy='subquery')
    product_fk = relationship(Product, lazy='subquery')


class ProductComment(Base):
    __tablename__ = 'product_comment'
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    assessment = Column(Integer)
    comment = Column(String)
    product_fk = relationship(Product, lazy='subquery')
