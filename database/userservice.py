from database.models import User
from database import get_db


def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()
    return all_users


def get_exact_user_db(user_id):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        return exact_user
    else:
        return 'С таким id пользователь не найден'


def register_user_db(name, phone_number, email, city, password, reg_date):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number).first()
    if checker:
        return 'Пользователь уже есть в БД'
    else:
        new_user = User(name=name, phone_number=phone_number, city=city, email=email, password=password,
                        reg_date=reg_date)
        db.add(new_user)
        db.commit()
        return 'Пользователь успешно зарегистртрован'


def login_user_db(email, password):
    db = next(get_db())
    checker = db.query(User).filter_by(email=email).first()
    if checker:
        if checker.password == password:
            return checker
        elif checker.password != password:
            return 'Неверный пароль'
    else:
        return 'Пользователь с таким email нет в БД'


def edit_user_data_db(user_id, edit_info, new_info):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_info == 'phone-number':
            exact_user.phone_number = new_info
        elif edit_info == 'email':
            exact_user.email = new_info
        elif edit_info == 'password':
            exact_user.password = new_info
        elif edit_info == 'city':
            exact_user.city = new_info

        db.commit()

        return 'Данные успешно изменены'
    else:
        return 'Этот пользователь еще не зарегистрирован'


def delete_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        db.delete(exact_user)
        db.commit()
        return 'Пользователь удален'
    else:
        return 'Пользователь не найден'


def check_phone_number_db(phone_number):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        return checker
    else:
        return 'Пользователь с таким номером нету в БД'
