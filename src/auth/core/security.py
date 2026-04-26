from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timedelta, timezone
from core.config import settings


def create_access_token(user_id, duration_token=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)):
    date_exp = datetime.now(timezone.utc) + duration_token
    
    dic = {"sub": str(user_id), "exp": date_exp}
    
    token = jwt.encode(dic, settings.SECRET_KEY,  algorithm=[settings.ALGORITHM])
    return token

def decode_access_token(token: str):
    try: 
        dic = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = str(dic.get("sub")) 
        return user_id
    except ExpiredSignatureError:
        return {'error': 'Token expirado'}
    except JWTError:
        return {'error': 'Token inválido'}
