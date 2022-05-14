import hashlib
import os


def hash_password_without_salt(password: str) -> str:
    hash_password = hashlib.sha256(password.encode("ascii")).hexdigest()
    return hash_password

def verify_password_without_salt(password: str, hash_password: str) -> bool:
    input_password = hashlib.sha256(password.encode("ascii")).hexdigest()
    return input_password == hash_password

def hash_password_with_salt(password: str) -> str:
    # creating salt
    random_size = 30
    salt = os.urandom(random_size)
    hashed_salt = hashlib.sha256(salt).hexdigest()

    # hashing password
    new_password = password + hashed_salt
    hashed_password = hashlib.sha256(new_password.encode("ascii")).hexdigest()

    combined_salt_and_password = ''.join([hashed_password, hashed_salt])

    return combined_salt_and_password

def verify_password_with_salt(password: str, hashed_password: str) -> bool:
    hashed_salt = hashed_password[-64:]
    new_password = password + hashed_salt
    password_to_check = hashlib.sha256(new_password.encode("ascii")).hexdigest()
    combined_salt_and_password = ''.join([password_to_check, hashed_salt])

    return combined_salt_and_password == hashed_password


