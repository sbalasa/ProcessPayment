import connexion
import six

from swagger_server.models.payment_item import PaymentItem  # noqa: E501
from swagger_server import util


def get_payment_info(card_holder, skip=None, limit=None):  # noqa: E501
    """Gets Payment Info

    Get the Payment Information  # noqa: E501

    :param card_holder: pass an optional search string for looking up Card Holder Details
    :type card_holder: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[PaymentItem]
    """
    return 'do some magic!'
