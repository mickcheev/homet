from users.entities import UserRegistration
from users.services import register_user

usr = UserRegistration(first_name = input('Enter first name: '), second_name = input('Enter second name: '),
                       email=input('Enter email: '), password=input('Enter password: '))

register_user.register_user(usr)