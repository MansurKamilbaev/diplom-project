from fastapi import APIRouter, UploadFile

from database.productservice import add_new_products_db, get_all_products_db, get_exact_products_db, \
    edit_products_data_db, delete_product_db, comment_product_db, get_all_comment_db, checker_product_db, \
    upload_product_photo, all_photos_db

from products import AddProductValidator, EditProductValidator, CommentProductValidator

product_router = APIRouter(prefix='/products', tags=['Работа с продуктами'])


@product_router.get('/products')
async def get_all_products():
    products = get_all_products_db()

    if products:
        return products
    else:
        return 'В БД пока нет  продуктов'


@product_router.post('/add-product')
async def add_product(data: AddProductValidator):
    new_product = data.model_dump()

    checker = checker_product_db(data.product_name)

    if checker:
        result = add_new_products_db(**new_product)
        return result
    else:
        return {'message': 'Продукт с таким названием уже есть'}


@product_router.post('/add-photo_product')
async def add_photo_product(product_id: int, photo_path: UploadFile = None):
    with open(f'media/{photo_path.filename}', 'wb') as file:
        product_photo = await photo_path.read()
        file.write(product_photo)

    result = upload_product_photo(product_id, f'/gallery/{photo_path.file}')

    if result:
        return {'message': result}
    else:
        return {'message': 'Возникла ошибка!'}


@product_router.get('/all-photo_product')
async def all_photos():
    result = all_photos_db()

    return result


@product_router.get('/product/{product_id}')
async def get_exact_product(product_id: int):
    product = get_exact_products_db(product_id)

    if product:
        return product
    else:
        return 'С таким айди нет продукта'


@product_router.put('/edit-product/{product_id}')
async def edit_products(data: EditProductValidator):
    edit_data = data.model_dump()
    new_data = edit_products_data_db(**edit_data)

    if new_data:
        return new_data
    else:
        return 'Не смогли изменить данные'


@product_router.post('/comment-product')
async def comment_product(data: CommentProductValidator):
    product = data.model_dump()
    result = comment_product_db(**product)

    if result:
        return {'message': 'Отзыв успешно добавлены!'}
    else:
        return {'message': 'Произошла ошибка в процессе добавления отзыва'}


@product_router.get('/get-all-comment')
async def get_all_comment_product():
    product = get_all_comment_db()

    if product:
        return product
    else:
        return 'В БД нет ни одного отзыва!'


@product_router.delete('/delete-product')
async def delete_product(product_id: int):
    product = delete_product_db(product_id=product_id)

    if product:
        return {'message': f'Благополучно удален продукт у которого айди: {product_id}'}
    else:
        return {'message': f'В БД нет продукта у которого айди равен: {product_id}'}
