from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django_testing.web.models import Profile


UserModel = get_user_model()


class ProfileListViewTests(TestCase):
    def test_get__expect_correct_template_name(self):
        response = self.client.get(reverse('list profiles'))

        self.assertEqual(response, 'profiles/list.html')

    def test_get__when_two_profiles__expect_context_to_contain_two_profiles(self):
        profiles_to_create = (
            Profile(first_name='Valery', last_name='Raikov', email='valery_r@gmail.com'),
            Profile(first_name='Meggie', last_name='Filipova', email='meggie@abv.bg'),
        )

        Profile.objects.bulk_create(profiles_to_create)

        response = self.client.get(reverse('list profiles'))

        profiles = response.context['object_list']

        self.assertEqual(len(profiles), 2)

    def test_get__when_no_loggedin_user_expect_context_user_to_be_No_user(self):
        response = self.client.get(reverse('list profiles'))

        self.assertEqual(response.context['user'], 'No user')

    def test_get__when_loggedin_user_expect_context_user_to_be_username(self):
        user_data = {
            'username': 'Valery',
            'password': 'Valerchi123',
        }

        UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)

        response = self.client.get(reverse('list profiles'))

        self.assertEqual(response.context['user'], response.user.username)
