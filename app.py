from flask import Flask, request, jsonify
from bot.chatBot import ChatbotTFIDF

app = Flask(__name__)
chatbot = ChatbotTFIDF()

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
