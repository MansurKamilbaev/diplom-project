from database.models import UserCart
from database import get_db


def get_all_products_to_cart_db():
    db = next(get_db())

    all_products = db.query(UserCart).all()

    return all_products


def delete_product_cart_db(product_id):
    db = next(get_db())

    product = db.query(UserCart).filter_by(product_id=product_id).first()

    if product:
        db.delete(product)
        db.commit()

        return f'Продукт с Айди: {product_id} успешно удален c корзины!'

    else:
        return f'Продукт с Айди: {product_id} не найден!'
