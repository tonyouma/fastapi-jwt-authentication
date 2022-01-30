# Responsible fro signing, encoding, decoding and returning JWTs

import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# Returns generated tokens
def token_response(token: str):
    return {
        "access token": token,
        # "token_type": "bearer",
    }

# Sign the JWT strings
def signJWT(userID: str):
    payload = {
        "userId": userID,
        "expires_in": time.time() + 60 * 60 * 24,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

# Decode JWT

def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decode_token if decode_token["expires"] >= time.time() else None
    except jwt.DecodeError:
        return {"error": "Invalid token"}
    except jwt.ExpiredSignatureError:
        return {"error": "Expired token"}
