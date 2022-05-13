import unittest
import copy

from users.entities import UserRegistration
from users.models import User
from users.services.register_user import register_user, delete_user
from users.services.user_login import login_user
from users.exceptions import InvalidUserData

testing_user = UserRegistration(
    first_name='Name', second_name='s name',
    email='sosisa12@mail.com', password='passwd',
)

changed_user = UserRegistration.parse_obj(testing_user.dict())
changed_user.email = 'email'


class UserLoginTestCase(unittest.TestCase):
    def setUp(self) -> None:
        register_user(testing_user)

    def tearDown(self) -> None:
        delete_user(testing_user.email)

    def test_user_login(self):
        self.assertEqual(login_user(testing_user), User.get(
            User.email == testing_user.email))

    def test_user_invalid_email(self):
        with self.assertRaises(InvalidUserData):
            login_user(changed_user)

    def test_user_invalid_password(self):
        changed_user.email = testing_user.email
        changed_user.password = 'another password'

        with self.assertRaises(InvalidUserData):
            login_user(changed_user)


if __name__ == '__main__':
    unittest.main()
