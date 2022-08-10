import json
from models import *
from config import db


def input_user_data(input_data):
    """ Функция для создания экземпляра User """
    for row in input_data:
        db.session.add(
            User(
                id=row.get("id"),
                first_name=row.get("first_name"),
                last_name=row.get("last_name"),
                age=row.get("age"),
                email=row.get("email"),
                role=row.get("role"),
                phone=row.get("phone")
            )
        )
    db.session.commit()


def input_order_data(input_data):
    """ Функция для создания экземпляра Order """
    for row in input_data:
        db.session.add(
            Order(
                id=row.get("id"),
                name=row.get("name"),
                description=row.get("description"),
                start_date=row.get("start_date"),
                end_date=row.get("end_date"),
                address=row.get("address"),
                price=row.get("price"),
                customer_id=row.get("customer_id"),
                executor_id=row.get("executor_id")
            )
        )
    db.session.commit()


def input_offer_data(input_data):
    """ Функция для создания экземпляра Offer """
    for row in input_data:
        db.session.add(
            Offer(
                id=row.get("id"),
                order_id=row.get("order_id"),
                executor_id=row.get("executor_id")
            )
        )
    db.session.commit()


def init_db():
    """ Функция для инициализации БД """
    db.drop_all()
    db.create_all()

    with open('data/user.json', encoding="utf-8") as f:
        input_user_data(json.load(f))

    with open('data/order.json', encoding="utf-8") as f:
        input_order_data(json.load(f))

    with open('data/offer.json', encoding="utf8") as f:
        input_offer_data(json.load(f))


def get_by_model(model):
    """ Получаем данные из БД """
    result = []
    query = model.query.all()
    for i in query:
        result.append(i.to_dict())
    return result


def get_by_id(model, user_id):
    """ Получаем данные из БД по id"""
    try:
        query = db.session.query(model).filter(model.id == user_id).all()[0].to_dict()
        return query
    except Exception:
        return {}


def get_update(model, user_id, values):
    """ Обновление данных """
    try:
        db.session.query(model).filter(model.id == user_id).update(values)
        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def delete_data(model, user_id):
    """ Обновление данных """
    try:
        db.session.query(model).filter(model.id == user_id).delete()
        db.session.commit()
    except Exception as e:
        print(e)
        return {}
