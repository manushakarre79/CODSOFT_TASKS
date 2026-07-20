from flask import Flask, render_template, request, jsonify
from datetime import datetime, date

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user = data["message"].lower().strip()

    if user in ["hi", "hello", "hey"]:
        reply = "Hello! How can I help you today?"

    elif user == "how are you":
        reply = "I'm doing great! Thanks for asking."

    elif user == "what is your name":
        reply = "My name is CodeSoft ChatBot."

    elif user == "who created you":
        reply = "I was created using Python and Flask."

    elif user == "what can you do":
        reply = "I can answer predefined questions."

    elif user == "time":
        reply = datetime.now().strftime("%I:%M:%S %p")

    elif user == "date":
        reply = str(date.today())

    elif user == "thank you":
        reply = "You're welcome!"

    elif user == "bye":
        reply = "Goodbye! Have a wonderful day."

    else:
        reply = "Sorry, I don't understand that."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)