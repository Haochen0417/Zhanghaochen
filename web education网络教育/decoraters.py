from bottle import request, redirect
from functools import wraps

def require_logged_in(sql_db):

    def inner(handler):
        @wraps(handler)
        def wrapper(*args, **kwargs):
            session = request.get_cookie('SESSIONID')
            if not session:
                return redirect('/login')
           
            userid = sql_db.get_user_id_from_session(session)

            if sql_db.session_is_expire(session):
                return redirect('/login')
            else:
                sql_db.update_expire_time(session)
            return handler(*args, **kwargs, userid=userid)
        return wrapper
    return inner

def secured():

    def inner(handler):
        @wraps(handler)
        def wrapper(*args, **kwargs):
            # banned_chars = ''

            banned_chars = '<>:"{}|[]\;\',/!#$%^&*()+-=~`'
            for arg in args:
                for char in banned_chars:
                    if char in arg:
                        return "<script> alert('Contains illegal characters!') </script>"

            return handler(*args, **kwargs)
        return wrapper
    return inner
