import os
import pymysql
from flask import Flask, jsonify

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "mysql-db")
DB_USER = os.environ.get("DB_USER", "flaskuser")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
DB_NAME = os.environ.get("DB_NAME", "flaskdb")


def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        connect_timeout=5
    )


@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "API Flask corriendo correctamente"}), 200


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/db-status")
def db_status():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"database": "connected"}), 200
    except Exception as e:
        return jsonify({"database": "error", "detail": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
