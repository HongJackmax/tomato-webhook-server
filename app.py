from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    message = data.get("text", "")
    sender = data.get("sender", {}).get("name", "알 수 없음")

    print(f"[{sender}] {message}")

    return jsonify({
        "text": f"✅ '{message}' 발주를 확인했습니다!"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
