from flask import request, jsonify
from src.core.calculator import Calculator
from src.utils.string_utils import capitalize_words

calc = Calculator()

def register_routes(app):

    @app.route("/calculate", methods=["POST"])
    def calculate():
        data = request.get_json()
        a = data.get("a")
        b = data.get("b")
        op = data.get("op")
        result = calc.compute(a, b, op)
        return jsonify({"result": result})

    @app.route("/format", methods=["POST"])
    def format_text():
        data = request.get_json()
        text = data.get("text", "")
        return jsonify({"formatted": capitalize_words(text)})

    @app.route("/history", methods=["GET"])
    def history():
        return jsonify({"history": calc.get_history()})
