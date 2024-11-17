from django.test import TestCase
from django.urls import reverse
from django_testing.web.models import Profile


class ProfileCreateViewTests(TestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Valery',
        'last_name': 'Raikov',
        'email': 'valery_r@gmail.com',
    }

    def test_create_profile__when_all_valid_expect_to_create(self):
        self.client.post(reverse('create profile'), data=self.VALID_PROFILE_DATA)

        profile = Profile.objects.first()

        self.assertIsNotNone(profile)
        self.assertEqual(self.VALID_PROFILE_DATA['first_name'], profile.first_name)
        self.assertEqual(self.VALID_PROFILE_DATA['last_name'], profile.last_name)
        self.assertEqual(self.VALID_PROFILE_DATA['email'], profile.email)

    def test_create_profile__when_all_valid_expect_to_redirect_to_details(self):
        response = self.client.post(reverse('create profile'), data=self.VALID_PROFILE_DATA)

        profile = Profile.objects.first()

        expected_url = reverse('profile details', kwargs={'pk': profile.pk})
        self.assertRedirects(response, expected_url)

    def test_create_profile__get_request_expect_status_code_200(self):
        response = self.client.get(reverse('create profile'))

        self.assertEqual(response.status_code, 200)

    def test_create_profile__post_request_expect_status_code_302(self):
        response = self.client.post(reverse('create profile'), data=self.VALID_PROFILE_DATA)

        self.assertEqual(response.status_code, 302)

    def test_create_profile__invalid_data_expect_status_code_400_or_200(self):
        invalid_data = {
            'first_name': '',
            'last_name': 'Raikov',
            'email': 'invalid_email_format',
        }

        response = self.client.post(reverse('create profile'), data=invalid_data)

        self.assertIn(response.status_code, [200, 400])
        self.assertTemplateUsed(response, 'profiles/create.html')
