# services/user_service.py
from sqlalchemy.orm import Session
from models.user import User
from core.security import create_token
from core.hashing import criptography, verify_password

def create_user(db: Session, name: str, email: str, password: str):
    user = User(
        name=name,
        email=email,
        hashed_password=criptography(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    token = create_token({"sub": user.user_id})

    return {"access_token": token, "token_type": "bearer", "user": user}


def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.user_id == user_id).first()