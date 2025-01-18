from flask import Flask, request, jsonify
from minio_utils import MinIOClient
from auth_utils import validate_jwt

app = Flask(__name__)

minio_client = MinIOClient(
    endpoint="http://localhost:9000",
    acces_key="admin",
    secret_key="password",
    bucket_name="file-storage"
)

@app.route('/upload', methods=['POST'])
@validate_jwt
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    response = minio_client.upload_file(file, file.filename)
    return jsonify(response)

@app.route('/download/<filename>', methods=['GET'])
@validate_jwt
def download_file(filename):
    response = minio_client.download_file(filename)
    if response['error']:
        return jsonify(response), 404
    return response['data'], 200

@app.route('/update/<filename>', methods=['PUT'])
@validate_jwt
def update_file(filename):
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    response = minio_client.upload_file(file, filename)
    return jsonify(response)

@app.route('/delete/<filename>', methods=['DELETE'])
@validate_jwt
def delete_file(filename):
    response = minio_client.delete_file(filename)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)