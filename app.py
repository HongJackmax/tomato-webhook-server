from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Tomato Webhook Server Running"

@app.route('/webhook', methods=['POST', 'HEAD', 'GET'])
def webhook():
    if request.method == 'HEAD':
        return '', 200
    if request.method == 'GET':
        return 'Webhook is alive', 200

    # POST 요청
    data = request.json
    print("Received Webhook Data:", data)
    return jsonify({
        "status": "success",
        "message": "Data received"
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

