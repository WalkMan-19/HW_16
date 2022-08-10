from flask import Blueprint, request
import json
from config import app
from utils import get_by_model, get_by_id, Offer, input_offer_data, get_update, delete_data

offer_blueprint = Blueprint('offer_blueprint', __name__)


@offer_blueprint.route('/offers/', methods=['GET', 'POST'])
def offers_page():
    if request.method == 'GET':
        data = get_by_model(Offer)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            input_offer_data(request.json)
        elif isinstance(request.json, dict):
            input_offer_data([request.json])
        else:
            print("Ошибка типа данных")
        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            mimetype="application/json"
        )


@offer_blueprint.route('/offers/<int:offer_id>', methods=['GET', 'PUT', 'DELETE'])
def offer_page(offer_id: int):
    if request.method == 'GET':
        data = get_by_id(Offer, offer_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        get_update(Offer, offer_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_data(Offer, offer_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            mimetype="application/json"
        )
