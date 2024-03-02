from database.models import Product, ProductComment, ProductPhoto
from database import get_db


def add_new_products_db(product_name, product_description, product_price, product_quantity):
    db = next(get_db())
    new_product = Product(product_name=product_name, product_description=product_description,
                          product_price=product_price, product_quantity=product_quantity)

    if new_product:
        db.add(new_product)
        db.commit()

        return 'Продукт успешно добавлен'

    else:
        return 'Ошибка при добавлении продукта'


def upload_product_photo(product_id, photo_path):
    db = next(get_db())

    new_photo = ProductPhoto(product_id=product_id, photo_path=photo_path)

    if new_photo:
        db.add(new_photo)
        db.commit()

        return 'Фото к продукту добавлен успешно!'
    else:
        return 'Нет продукта'


def all_photos_db():
    db = next(get_db())

    photos = db.query(ProductPhoto).all()

    return photos


def get_all_products_db():
    db = next(get_db())

    all_products = db.query(Product).all()

    return all_products


def get_exact_products_db(product_id):
    db = next(get_db())

    exact_product = db.query(Product).filter_by(product_id=product_id).first()

    if exact_product:
        return exact_product
    else:
        return f'Такого продукта с Айди: {product_id} не сущетвует'


def edit_products_data_db(product_id, edit_data, new_data):
    db = next(get_db())

    get_product = db.query(Product).filter_by(product_id=product_id).first()

    if get_product:
        if edit_data == 'product-name':
            get_product.product_name = new_data
        elif edit_data == 'product-description':
            get_product.product_description = new_data
        elif edit_data == 'product-price':
            get_product.product_price = new_data
        elif edit_data == 'product-quantity':
            get_product.product_quantity = new_data

        db.commit()
        return 'Данные успешно изменены'
    else:
        return 'Этот продукт не найден в БД'


def delete_product_db(product_id):
    db = next(get_db())

    product = db.query(Product).filter_by(product_id=product_id).first()

    if product:
        db.delete(product)
        db.commit()

        return f'Продукт с Айди: {product_id} успешно удален!'

    else:
        return f'Продукт с Айди: {product_id} не найден!'


def comment_product_db(product_id, assessment, comment):
    db = next(get_db())

    add_comment = ProductComment(product_id=product_id, assessment=assessment, comment=comment)

    if add_comment:
        db.add(add_comment)
        db.commit()

        return 'Отзыв успешно добавлен!'
    else:
        return 'Отзыв для данного продукта не найдены.'


def get_all_comment_db():
    db = next(get_db())
    result = db.query(ProductComment).all()

    if result:
        return result
    else:
        return 'Нету ни одного отзыва!'


def checker_product_db(product_name):
    db = next(get_db())
    checker = db.query(Product).filter_by(product_id=product_name).first()

    if checker:
        return checker
    else:
        return f'Нету такого продукта'
