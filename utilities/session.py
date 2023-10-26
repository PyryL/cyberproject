from flask import session
from secrets import token_hex

class Session:
    @classmethod
    def check_user_id(cls, request):
        if session.get("user_id") is not None:
            return session.get("user_id")
        if request.cookies.get("user_id") is not None:
            return request.cookies.get("user_id")
        return None

    @classmethod
    def csrf_token(cls) -> str:
        if session.get("csrf_token") is not None:
            return session.get("csrf_token")
        token = token_hex(16)
        session["csrf_token"] = token
        return token
