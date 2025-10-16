from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
import jwt
import os
from data.users import users

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

SECRET_KEY = os.getenv("JWT_SECRET")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Email dan password wajib diisi"}), 400

    user = next((u for u in users if u["email"] == data["email"] and u["password"] == data["password"]), None)
    if not user:
        return jsonify({"error": "Email atau password salah"}), 401

    exp_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = jwt.encode({
        "sub": user["id"],
        "email": user["email"],
        "exp": exp_time
    }, SECRET_KEY, algorithm="HS256")

    return jsonify({
        "access_token": token,
        "token_type": "bearer",
        "expires_at": exp_time.isoformat()
    }), 200
