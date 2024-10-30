# app.py
from flask import Flask, render_template, request, jsonify
from chatbot import chat_with_gpt

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/solve_error", methods=["POST"])
def solve_error():
    data = request.get_json()
    target = data.get("target")
    error = data.get("error")
    program = data.get("program")

    if not (target and error and program):
        return jsonify({"error": "Please provide target, error, and program details."}), 400

    try:
        response = chat_with_gpt(target, error, program)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
