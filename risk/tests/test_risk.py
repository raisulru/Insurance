import json
import random
from faker import Faker
from django.urls import reverse
from insurance.test_case import InsuranceTestCase
from risk.tests import RiskFactory, FieldTypeFactory, UserFactory
from ..models import Risk, FieldType
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

        request = self.client.get(self.url)
        self.assertSuccess(request)


        field1 = FieldTypeFactory()

        field2 = FieldTypeFactory()

        self.assertEqual(FieldType.objects.count(), 2)

        risk = RiskFactory.create(fields=(field1, field2))

        request = self.client.get(self.url)
        self.assertSuccess(request)

        self.assertEqual(Risk.objects.count(), 1)

        field3 = FieldTypeFactory()

        field4 = FieldTypeFactory()

        self.assertEqual(FieldType.objects.count(), 4)

        risk = RiskFactory.create(fields=(field1, field2, field3, field4))
        self.assertEqual(Risk.objects.count(), 2)

        self.client.logout()


    def test_risk_list_post(self):

        data = {
            'name': self.fake.first_name(),
            'fields': FieldTypeFactory()
        }

        login = self.client.login(username='admin', password='adm1n')
        self.assertTrue(login)
        
        request = self.client.post(self.url, data)
        self.assertCreated(request)
#         self.assertEqual(Accounts.objects.count(), 1)
#         self.assertEqual(request.data['name'], data['name'])
#         self.assertEqual(request.data['description'], data['description'])
#         self.assertEqual(request.data['type'], data['type'])
#         self.assertEqual(
#             request.data['opening_balance'], data['opening_balance'])

#         # admin user logout
#         self.client.logout()


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
