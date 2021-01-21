from datetime import datetime
from cardvalidator import luhn
from collections import defaultdict
from flask import abort, Flask, request, jsonify

app = Flask(__name__)

payments = defaultdict(dict)


def validate_content(content):
    required_fields = {"CreditCardNumber", "CardHolder", "ExpirationDate", "Amount"}
    if not all(i in content for i in required_fields):
        return abort(400)
    if not luhn.is_valid(content["CreditCardNumber"]):
        return abort(400)
    if not datetime(*map(int, content["ExpirationDate"].split("-"))) > datetime.now():
        return abort(400)
    if not content["Amount"] >= 0:
        return abort(400)
    else:
        amount = content["Amount"]
        payment_gateway = ""
        if amount < 20:
            payment_gateway = "CheapPaymentGateway"
        elif 21 < amount < 500:
            payment_gateway = "ExpensivePaymentGateway"
        elif amount > 500:
            payment_gateway = "PremiumPaymentGateway"
        content.update({"PaymentGateway": payment_gateway})
        payments[content["CardHolder"]] = content
        return content


@app.route("/")
def index():
    return "<html><h1>Welcome to Process Payment REST API</h1></html>"


@app.route("/ProcessPayment", methods=["GET", "POST"])
def process_payment():
    if request.method == "GET":
        card_holder = request.args.get("CardHolder")
        return jsonify(payments[card_holder])
    elif request.method == "POST":
        return jsonify(validate_content(request.json))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
