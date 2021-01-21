# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.payment_item import PaymentItem  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def test_get_payment_info(self):
        """Test case for get_payment_info

        Gets Payment Info
        """
        query_string = [('card_holder', 'card_holder_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/ProcessPayments',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
