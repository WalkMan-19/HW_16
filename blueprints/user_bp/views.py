from flask import Blueprint, request
import json
from config import app
from utils import get_by_model, get_by_id, User, input_user_data, get_update, delete_data

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/users/', methods=['GET', 'POST'])
def users_page():
    if request.method == 'GET':
        data = get_by_model(User)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            input_user_data(request.json)
        elif isinstance(request, dict):
            input_user_data([request.json])
        else:
            print('Ошибка типа данных')
        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            mimetype="application/json"
        )


@user_blueprint.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_page(user_id: int):
    if request.method == 'GET':
        data = get_by_id(User, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        get_update(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_data(User, user_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            mimetype="application/json"
        )
