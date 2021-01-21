import app
import unittest


from flask import json


class ProcessPaymentTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_get(self):
        response = self.app.get("/ProcessPayment")
        assert response.status_code == 200
        self.assertIn(b"{}", response.data)

    def test_post(self):
        data = {
            "Amount": 13.45,
            "CardHolder": "Santee Cooper",
            "CreditCardNumber": "5500000000000004",
            "ExpirationDate": "2023-04-12",
            "PaymentGateway": "CheapPaymentGateway",
            "SecurityCode": 232,
        }
        response = self.app.post("/ProcessPayment", data=json.dumps(data), content_type="application/json")
        post_response = json.loads(response.get_data(as_text=True))
        post_response.update({"PaymentGateway": "CheapPaymentGateway"})
        assert response.status_code == 200
        assert post_response == data
