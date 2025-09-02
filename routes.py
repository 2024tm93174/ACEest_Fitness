# routes.py
from flask import Blueprint, jsonify, request

bp = Blueprint("bp", __name__)

@bp.route("/ping")
def ping():
    return jsonify({"message": "pong"}), 200

@bp.route("/echo", methods=["POST"])
def echo():
    data = request.json
    if not data or "msg" not in data:
        return jsonify({"error": "Missing field 'msg'"}), 400
    return jsonify({"echo": data["msg"]}), 201
