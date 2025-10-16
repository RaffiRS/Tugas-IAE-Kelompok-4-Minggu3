from flask import Blueprint, jsonify, request
from data.users import users
import jwt
import os

profile_bp = Blueprint("profile", __name__, url_prefix="/profile")

SECRET_KEY = os.getenv("JWT_SECRET")

def decode_token(auth_header):
    if not auth_header:
        return None, "Authorization header missing"
    try:
        token = auth_header.split(" ")[1]
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded, None
    except jwt.ExpiredSignatureError:
        return None, "Token expired"
    except jwt.InvalidTokenError:
        return None, "Invalid token"

@profile_bp.route("", methods=["PUT"])
def update_profile():
    auth_header = request.headers.get("Authorization")
    decoded, error = decode_token(auth_header)

    if error:
        return jsonify({"error": error}), 401

    user = next((u for u in users if u["id"] == decoded["sub"]), None)
    if not user:
        return jsonify({"error": "User tidak ditemukan"}), 404

    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Field 'name' wajib diisi"}), 400

    user["name"] = data["name"]
    return jsonify({
        "message": "Profil berhasil diperbarui",
        "user": {"id": user["id"], "email": user["email"], "name": user["name"]}
    }), 200
