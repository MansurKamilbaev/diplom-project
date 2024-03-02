from fastapi import APIRouter

from database.models import UserCart
from database.user_cartservice import get_all_products_to_cart_db, delete_product_cart_db

from database import get_db

cart_router = APIRouter(prefix='/cart', tags=['Корзина'])


@cart_router.post("/add_product_to_cart/{user_id}/{product_id}/{quantity}")
async def add_product_to_cart(user_id: int, product_id: int, product_quantity: int):
    db = next(get_db())
    user_cart = UserCart(user_id=user_id, product_id=product_id, quantity=product_quantity)
    db.add(user_cart)
    db.commit()
    return {"message": "Продукт успешно добавлен в корзину"}


@cart_router.get('/all-products_cart')
async def get_all_products():
    all_product_to_cart = get_all_products_to_cart_db()

    if all_product_to_cart:
        return all_product_to_cart
    else:
        return 'В БД пока нет  продуктов'


@cart_router.delete('/remove-product_cart')
async def remove_product_to_cart(product_id):
    product = delete_product_cart_db(product_id=product_id)

    if product:
        return {'message': f'Успешно  удален из корзины продукт у которого айди: {product_id}'}
    else:
        return {'message': f'В БД нет продукта у которого айди равен: {product_id}'}
