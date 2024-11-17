from django.test import TestCase
from django.core.exceptions import ValidationError
from django_testing.web.models import Account, Profile


class AccountTests(TestCase):
    VALID_ACCOUNT_DATA = {
        'username': 'Valeri_R12',
        'password': 'somePass123',
        'isBanned': False,
    }

    def setUp(self):
        self.profile = Profile.objects.create(
            first_name='Valery',
            last_name='Raikov',
            email='valery_r@gmail.com',
        )

        self.VALID_ACCOUNT_DATA['profile'] = self.profile

    def test_account_create__when_username_is_alphanumeric__expect_success(self):
        account = Account.objects.create(**self.VALID_ACCOUNT_DATA)
        self.assertIsNotNone(account)
        self.assertEqual(account.username, self.VALID_ACCOUNT_DATA['username'])

    def test_account_create__when_username_contains_a_question_mark__expect_failure(self):
        wrong_username = 'Val?ery_R'

        with self.assertRaises(ValidationError) as context:
            account = Account.objects.create(
                username=wrong_username,
                password=self.VALID_ACCOUNT_DATA['password'],
                is_banned=self.VALID_ACCOUNT_DATA['is_banned'],
                profile=self.profile,
            )

            account.full_clean()

        self.assertIsNotNone(context.exception)

    def test_account_create__when_username_contains_a_space__expect_failure(self):
        wrong_username = 'Valery R'

        with self.assertRaises(ValidationError) as context:
            account = Account.objects.create(
                username=wrong_username,
                password=self.VALID_ACCOUNT_DATA['password'],
                is_banned=self.VALID_ACCOUNT_DATA['is_banned'],
                profile=self.profile,
            )

            account.full_clean()

        self.assertIsNotNone(context.exception)
