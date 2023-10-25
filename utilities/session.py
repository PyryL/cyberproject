from flask import session

class Session:
    @classmethod
    def check_user_id(cls, request):
        if session.get("user_id") is not None:
            return session.get("user_id")
        if request.cookies.get("session") is not None:
            return request.cookies.get("session")
        return None
