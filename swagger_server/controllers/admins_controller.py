import connexion
import six

from swagger_server.models.payment_item import PaymentItem  # noqa: E501
from swagger_server import util


def add_payment_info(body=None):  # noqa: E501
    """Processes Credit Card Payments

    Adds an item to the system # noqa: E501

    :param body: Payment item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PaymentItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
