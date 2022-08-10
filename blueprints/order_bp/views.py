from flask import Blueprint, request
import json
from config import app
from utils import get_by_model, get_by_id, Order, input_order_data, get_update, delete_data

order_blueprint = Blueprint('order_blueprint', __name__)


@order_blueprint.route('/orders/', methods=['GET', 'POST'])
def orders_page():
    if request.method == 'GET':
        data = get_by_model(Order)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            input_order_data(request.json)
        elif isinstance(request, dict):
            input_order_data([request.json])
        else:
            print('Ошибка типа данных')
        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            mimetype="application/json"
        )


@order_blueprint.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def order_page(order_id: int):
    if request.method == 'GET':
        data = get_by_id(Order, order_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        get_update(Order, order_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_data(Order, order_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            mimetype="application/json"
        )
