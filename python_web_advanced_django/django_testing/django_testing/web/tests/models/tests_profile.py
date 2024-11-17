from django.test import TestCase
from django.core.exceptions import ValidationError
from django_testing.web.models import Profile


class ProfileTests(TestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Valery',
        'last_name': 'Raikov',
        'email': 'valery_r@gmail.com',
    }

    def test_profile_create__when_first_name_contains_only_letters__excpect_success(self):
        profile = Profile.objects.create(**self.VALID_PROFILE_DATA)
        self.assertIsNotNone(profile)

    def test_profile_create__when_first_name_contains_a_digit__excpect_failure(self):
        wrong_first_name = 'Valery7'

        with self.assertRaises(ValidationError) as context:
            profile = Profile.objects.create(
                first_name=wrong_first_name,
                last_name=self.VALID_PROFILE_DATA['last_name'],
                email=self.VALID_PROFILE_DATA['email'],
            )

            profile.full_clean()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_dollar_sign__excpect_failure(self):
        wrong_first_name = 'Va$lery'

        with self.assertRaises(ValidationError) as context:
            profile = Profile.objects.create(
                first_name=wrong_first_name,
                last_name=self.VALID_PROFILE_DATA['last_name'],
                email=self.VALID_PROFILE_DATA['email'],
            )

            profile.full_clean()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_space__excpect_failure(self):
        wrong_first_name = 'Vale ry'

        with self.assertRaises(ValidationError) as context:
            profile = Profile.objects.create(
                first_name=wrong_first_name,
                last_name=self.VALID_PROFILE_DATA['last_name'],
                email=self.VALID_PROFILE_DATA['email'],
            )

            profile.full_clean()

        self.assertIsNotNone(context.exception)

    def test_profile_full_name__when_valid__excpect_correct_full_name(self):
        profile = Profile.objects.create(**self.VALID_PROFILE_DATA)

        expected_full_name = f'{self.VALID_PROFILE_DATA["first_name"]} {self.VALID_PROFILE_DATA["last_name"]}'
        self.assertEqual(expected_full_name, profile.full_name)
