import unittest

from users.services.register_user import register_user, check_existence
from users.entities import UserRegistration
from users.models import User
from users.exceptions import UserAlreadyExists


testing_user = UserRegistration(
            first_name='Name', second_name='s name',
            email='sosiso4ka@mail.com', password='passwd',
        )


class RegistrationUserTest(unittest.TestCase):
    def test_user_registration(self):
        db_user = register_user(testing_user)
        self.assertEqual(db_user, User.get(User.email == testing_user.email))

    def test_user_existence(self):
        db_user = register_user(testing_user)
        with self.assertRaises(UserAlreadyExists):
            check_existence(testing_user)

    def tearDown(self) -> None:
        User.delete().where(User.email == 'sosiso4ka@mail.com').execute()


if __name__ == '__main__':
    unittest.main()
