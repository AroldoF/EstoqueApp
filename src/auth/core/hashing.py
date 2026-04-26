from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def criptography(password: str):
    encrypted_pass = bcrypt_context.hash(password)
    return encrypted_pass

def verify_password(password: str, hashed_password: str):
    is_valid = bcrypt_context.verify(password, hashed_password)
    return is_valid