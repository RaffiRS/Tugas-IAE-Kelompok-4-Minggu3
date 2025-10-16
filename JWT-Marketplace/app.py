from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from routes.auth_routes import auth_bp
from routes.item_routes import item_bp
from routes.profile_routes import profile_bp

load_dotenv()

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(item_bp)
app.register_blueprint(profile_bp)

@app.route("/", methods=["GET"])
def home():
    return {"message": "API berjalan dengan baik!"}, 200

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint tidak ditemukan"}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method tidak diizinkan"}), 405

@app.errorhandler(415)
def unsupported_media_type(error):
    return jsonify({"error": "Content-Type harus application/json"}), 415

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Terjadi kesalahan internal server"}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=True)