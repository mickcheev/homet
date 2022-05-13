import unittest

from notes.services.manage_nodes import delete_node
from notes.models import Node
from users.tests.user_login_test import testing_user
from users.services.register_user import register_user, delete_user


class NoteManageTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.user = register_user(testing_user)
        self.prime_node = Node.get(Node.owner == self.user, Node.prime == True)

    def test_prime_node(self):
        self.assertIsNotNone(self.prime_node)

    def tearDown(self) -> None:
        delete_user(user_email=self.user.email)
        delete_node(self.prime_node.id)


if __name__ == '__main__':
    unittest.main()

