from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from e_commerce.apps.users.models import User
from e_commerce.apps.users.views import UserListCreateView


class UserCreationTest(APITestCase):
    def setUp(self):
        self.view = UserListCreateView.as_view({"get": "list", 
                                                    "post": "create"} )
        self.url = reverse('user-list')

    def test_user_creation_with_missing_credentials(self):
        """
        This test checks user creation without required input data. The scenarios are,
            - Empty input data
            - Input data without 'password2'
            - Input data without 'password'
        """

        # Empty input data
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {
                                    'full_name': ['This field is required.'],
                                     'password': ['This field is required.'],
                                      'password2': ['This field is required.'],
                                       'username': ['This field is required.']
                        } )


        # Input data without 'password2'
        response = self.client.post(self.url, {
            "full_name": 'Test User 2',
            "password": "test-password",
            'username': "testUser2"
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {
                            'password2': ['This field is required.']
                        } )


        # Input data without 'password'
        response = self.client.post(self.url, {
            "full_name": 'Test User 3',
            "password2": "test-password",
            'username': "testUser3"
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {
                            'password': ['This field is required.']
                        } )

    def test_user_cration_is_succesful(self):
        """

        """
        response = self.client.post(self.url, {
            "full_name": 'Test User',
            "password": "test-password",
            "password2": "test-password",
            'username': "testUser"
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
                                'full_name': 'Test User', 
                                'email': '', 
                                'username': 'testUser'
                        } )

    def test_user_creation_with_unmatched_passwords(self):
        """
        This test proves it is not possible to create a user with umatched passwords ('password' and 'password2').
        """

        # 'password' and 'password2' are not equal
        response = self.client.post(self.url, {
            "full_name": 'Test User 4',
            "password": "test-passwor",
            "password2": "not equal to 'password'",
            'username': "testUser4"
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {
                            'non_field_errors': [
                                "'password' attribute should be euqal to 'password2'"
                            ]
                        })
