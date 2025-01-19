import requests
from flask import request, jsonify

def validate_jwt(func):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"error": "Missing or invalid token"}), 401

        token = auth_header.split(' ')[1]
        try:
            response = requests.get(
                "http://keycloak:8080/realms/file-management/protocol/openid-connect/userinfo",
                headers={"Authorization": f"Bearer {token}"}
            )
            if response.status_code != 200:
                return jsonify({"error": "Invalid token"}), 401
        except requests.RequestException as e:
            return jsonify({"error": str(e)}), 500

        return func(*args, **kwargs)
    return wrapper