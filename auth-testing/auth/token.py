import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "supersecret"

def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(seconds=10)
    }
    print('🪙 Generating token.')
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token):
    try:
        print('👀 Validating token.')
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        print("⌛️ Token expired\n")
        return None
    except jwt.InvalidTokenError:
        print('❌ Invalid token\n')
        return None


