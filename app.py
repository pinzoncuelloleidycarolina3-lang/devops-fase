import os
from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# ⚠️  VULNERABILIDAD INTENCIONAL — Bandit B105
# Credencial quemada en código fuente
DB_PASSWORD = "SuperSecreta123!"   # <-- esto dispara Bandit HIGH
DB_HOST     = os.getenv("DB_HOST", "db")
DB_NAME     = os.getenv("MYSQL_DATABASE", "impulsapro")

def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user="root",
        password=DB_PASSWORD,   # hardcoded
        database=DB_NAME,
    )

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)