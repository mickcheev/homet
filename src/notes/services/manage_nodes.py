from notes.entities import NewNode
from notes.models import Node as Model
from users.models import User


def create_node(node: NewNode, user: User):
    Model.create(parent=node.parent, owner=user, name=node.name)


def create_prime_node(user: User):
    Model.create(owner=user, prime=True, name='notes')


def delete_node(node_id: int):
    Model.delete().where(Model.id == node_id).execute()
