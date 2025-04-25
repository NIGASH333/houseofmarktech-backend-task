def generate_token(user_id):
    import jwt
    import datetime

    token = jwt.encode({
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, 'your_secret_key', algorithm='HS256')

    return token

def decode_token(token):
    import jwt

    try:
        data = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
        return data['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def is_authenticated(token):
    user_id = decode_token(token)
    return user_id is not None

def validate_token(token):
    import jwt

    try:
        jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
        return True
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return False