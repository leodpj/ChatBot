from flask import Flask, request, jsonify
from chatbot_logic import get_response
from database import init_db, save_message

app = Flask(__name__)
init_db()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = get_response(user_message)

    # Salvar no banco
    save_message("user", user_message)
    save_message("bot", bot_response)

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
