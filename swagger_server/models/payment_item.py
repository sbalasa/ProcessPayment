# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PaymentItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, credit_card_number: str=None, card_holder: str=None, expiration_date: datetime=None, security_code: int=None, amount: float=None):  # noqa: E501
        """PaymentItem - a model defined in Swagger

        :param credit_card_number: The credit_card_number of this PaymentItem.  # noqa: E501
        :type credit_card_number: str
        :param card_holder: The card_holder of this PaymentItem.  # noqa: E501
        :type card_holder: str
        :param expiration_date: The expiration_date of this PaymentItem.  # noqa: E501
        :type expiration_date: datetime
        :param security_code: The security_code of this PaymentItem.  # noqa: E501
        :type security_code: int
        :param amount: The amount of this PaymentItem.  # noqa: E501
        :type amount: float
        """
        self.swagger_types = {
            'credit_card_number': str,
            'card_holder': str,
            'expiration_date': datetime,
            'security_code': int,
            'amount': float
        }

        self.attribute_map = {
            'credit_card_number': 'CreditCardNumber',
            'card_holder': 'CardHolder',
            'expiration_date': 'ExpirationDate',
            'security_code': 'SecurityCode',
            'amount': 'Amount'
        }
        self._credit_card_number = credit_card_number
        self._card_holder = card_holder
        self._expiration_date = expiration_date
        self._security_code = security_code
        self._amount = amount

    @classmethod
    def from_dict(cls, dikt) -> 'PaymentItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PaymentItem of this PaymentItem.  # noqa: E501
        :rtype: PaymentItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def credit_card_number(self) -> str:
        """Gets the credit_card_number of this PaymentItem.


        :return: The credit_card_number of this PaymentItem.
        :rtype: str
        """
        return self._credit_card_number

    @credit_card_number.setter
    def credit_card_number(self, credit_card_number: str):
        """Sets the credit_card_number of this PaymentItem.


        :param credit_card_number: The credit_card_number of this PaymentItem.
        :type credit_card_number: str
        """
        if credit_card_number is None:
            raise ValueError("Invalid value for `credit_card_number`, must not be `None`")  # noqa: E501

        self._credit_card_number = credit_card_number

    @property
    def card_holder(self) -> str:
        """Gets the card_holder of this PaymentItem.


        :return: The card_holder of this PaymentItem.
        :rtype: str
        """
        return self._card_holder

    @card_holder.setter
    def card_holder(self, card_holder: str):
        """Sets the card_holder of this PaymentItem.


        :param card_holder: The card_holder of this PaymentItem.
        :type card_holder: str
        """
        if card_holder is None:
            raise ValueError("Invalid value for `card_holder`, must not be `None`")  # noqa: E501

        self._card_holder = card_holder

    @property
    def expiration_date(self) -> datetime:
        """Gets the expiration_date of this PaymentItem.


        :return: The expiration_date of this PaymentItem.
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date: datetime):
        """Sets the expiration_date of this PaymentItem.


        :param expiration_date: The expiration_date of this PaymentItem.
        :type expiration_date: datetime
        """
        if expiration_date is None:
            raise ValueError("Invalid value for `expiration_date`, must not be `None`")  # noqa: E501

        self._expiration_date = expiration_date

    @property
    def security_code(self) -> int:
        """Gets the security_code of this PaymentItem.


        :return: The security_code of this PaymentItem.
        :rtype: int
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code: int):
        """Sets the security_code of this PaymentItem.


        :param security_code: The security_code of this PaymentItem.
        :type security_code: int
        """
        if security_code is None:
            raise ValueError("Invalid value for `security_code`, must not be `None`")  # noqa: E501

        self._security_code = security_code

    @property
    def amount(self) -> float:
        """Gets the amount of this PaymentItem.


        :return: The amount of this PaymentItem.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        """Sets the amount of this PaymentItem.


        :param amount: The amount of this PaymentItem.
        :type amount: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount