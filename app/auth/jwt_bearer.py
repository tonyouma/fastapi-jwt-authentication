# The function checks whether the request is authenticated or not.

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_handler import decodeJWT

class jwtBearer(HTTPBearer):
    def __init__(self, auto_Error: bool =True):
        super(jwtBearer, self).__init__(auto_error=auto_Error)
        # self.scheme = "Bearer"

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme != "Bearer":
                raise HTTPException(status_code=403, detail="Invalid or Expired Token")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid or Expired Token")

    def verify_jwt(self, jwtToken: str):
        isTokenvalid: bool = False
        payload = decodeJWT(jwtToken)
        if payload:
            isTokenvalid = True
        return isTokenvalid