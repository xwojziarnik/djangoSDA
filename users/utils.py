import hashlib


def hash_password_without_salt(password: str) -> str:
    hash_password = hashlib.sha256(password.encode("ascii")).hexdigest()
    return hash_password

def verify_password_without_salt(password: str, hash_password: str) -> bool:
    input_password = hashlib.sha256(password.encode("ascii")).hexdigest()
    return input_password == hash_password
