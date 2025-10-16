from flask import Blueprint, jsonify
from data.items import items

item_bp = Blueprint("items", __name__, url_prefix="/items")

@item_bp.route("", methods=["GET"])
def get_items():
    return jsonify({"items": items}), 200
