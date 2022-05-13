import hashlib


def hash_password(source_passwd: str) -> str:
    h = hashlib.new('sha256')
    h.update(str(source_passwd).encode('utf-8'))
    return h.hexdigest()
