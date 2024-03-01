from fastapi import APIRouter

from database.userservice import get_all_users_db, get_exact_user_db, register_user_db, login_user_db, \
    edit_user_data_db, delete_user_db, check_phone_number_db

from datetime import datetime

from users import RegistrationValidator, Login, EditUserValidator

user_router = APIRouter(prefix='/users', tags=['Работа с пользователями'])


@user_router.post('/register')
async def register_new_user(data: RegistrationValidator):
    new_user = data.model_dump()

    checker = check_phone_number_db(data.phone_number)

    if checker:
        result = register_user_db(reg_date=datetime.now(), **new_user)
        return result
    else:
        return {'message': 'Пользователь с таким телефон номером уже существует'}


@user_router.post('/login')
async def login_user(data: Login):
    result = login_user_db(**data.model_dump())
    if result:
        return result
    else:
        return 'Такого пользователя нет в БД'


@user_router.get('/all-users')
async def gett_all_users():
    all_users = get_all_users_db()

    if all_users:
        return all_users
    else:
        return 'В БД нету пока что зарегистрированных пользователей'


@user_router.get('/get-exact-user_information')
async def get_exact_user_info(user_id):
    user_info = get_exact_user_db(user_id)
    if user_info:
        return {'Информация про пользователя': user_info}
    else:
        return 'Пользователь не найден в БД'


@user_router.put('/edit-user-data')
async def edit_user_data(data: EditUserValidator):
    edited_data = data.model_dump()
    new_data = edit_user_data_db(**edited_data)

    return new_data


@user_router.delete('/delete-user')
async def delete_user(user_id):
    user = delete_user_db(user_id)

    if user:
        return 'Пользователь удален'
    else:
        return 'В БД нету такого пользователья'
