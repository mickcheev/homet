import hashlib


def hash_password(source_passwd: str) -> str:
    h = hashlib.new('sha256')
    h.update(bytes(source_passwd, 'utf-8'))
    return h.hexdigest()


print(hash_password('приветр'))

