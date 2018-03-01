import json
import random
import factory
from faker import Faker
from django.urls import reverse
from insurance.test_case import InsuranceTestCase
from risk.tests import (
    RiskFactory,
    UserFactory,
    ChoicesFieldFactory,
    FieldsFactory,
    RiskTypeFactory,
    RisksFieldsFactory,
    RisksWithFieldsFactory,
    RisksWith2FieldsFactory
    )
from ..models import Risk, Fields
from ..enums import FIELD_TYPES


class RiskListAPITest(InsuranceTestCase):
    url = reverse('risk-list')
    fake = Faker()

    def setUp(self):
        super(RiskListAPITest, self).setUp()

    def test_risk_list_get(self):
        #  Check without login
        request = self.client.get(self.url)
        self.assertSuccess(request)

        #  Check with login
        login = self.client.login(username='admin', password='adm1n')
        self.assertTrue(login)

        RisksWithFieldsFactory()

        request = self.client.get(self.url)
        self.assertSuccess(request)

        RisksWith2FieldsFactory()

        self.assertEqual(Risk.objects.count(), 3)

        self.client.logout()


    def test_risk_list_post(self):
        login = self.client.login(username='admin', password='adm1n')
        self.assertTrue(login)

        data = {
            'name': self.fake.first_name(),
            'risk_type': RiskTypeFactory().pk,
            'field_items': json.dumps([
                {
                    "field_name": self.fake.first_name(),
                    "field_type": 1,
                    "char_field": self.fake.first_name(),
                    "text_field": 'n/a',
                    "email_field": None,
                    "boolean_field": False,
                    "date_time_field": None,
                    "file_field": None,
                    "image_field": None,
                    "decimal_field": None,
                    "float_field": None,
                    "time_field": None,
                    "url_field": "None",
                    "choices_field": {
                        "name": self.fake.first_name()
                    }
                },
                {
                    "field_name": self.fake.first_name(),
                    "field_type": 2,
                    "char_field": None,
                    "text_field": 'This is Text Fields',
                    "email_field": None,
                    "boolean_field": False,
                    "date_time_field": None,
                    "file_field": None,
                    "image_field": None,
                    "decimal_field": None,
                    "float_field": None,
                    "time_field": None,
                    "url_field": "None",
                    "choices_field": None
                }
            ]),
        }

        request = self.client.post(self.url, data)
        self.assertCreated(request)

        request = self.client.get(self.url)
        self.assertSuccess(request)

        # print(request.data)
#         self.assertEqual(Accounts.objects.count(), 1)
#         self.assertEqual(request.data['name'], data['name'])
#         self.assertEqual(request.data['description'], data['description'])
#         self.assertEqual(request.data['type'], data['type'])
#         self.assertEqual(
#             request.data['opening_balance'], data['opening_balance'])

#         # admin user logout
        self.client.logout()


# class AccountDetailsAPITest(OmisTestCase):
#     url = None
#     fake = Faker()

#     def setUp(self):
#         super(AccountDetailsAPITest, self).setUp()

#         # set a transaction head
#         self.admin_user_account = AccountFactory(
#             organization=self.user.organization)

#         # set the url
#         self.url = reverse('accounts-details',
#                            args=[self.admin_user_account.alias])

#     def test_account_details_get(self):
#         # ===========================================
#         #  Check without login
#         # ===========================================
#         request = self.client.get(self.url)
#         self.assertPermissionDenied(request)

#         # ===========================================
#         #  Check with login
#         # ===========================================
#         login = self.client.login(phone=self.user.phone, password='testpass')
#         self.assertTrue(login)
#         request = self.client.get(self.url)
#         self.assertPermissionDenied(request)

#         # user logout
#         self.client.logout()

#         # ===========================================
#         #  Check with admin user
#         # ===========================================
#         login = self.client.login(
#             phone=self.admin_user.phone, password='testpass')
#         self.assertTrue(login)
#         request = self.client.get(self.url)

#         self.assertSuccess(request)
#         self.assertEqual(request.data['id'], self.user.id)

#         # admin user logout
#         self.client.logout()
