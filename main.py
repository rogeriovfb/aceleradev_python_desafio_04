import jwt


def create_token(data, secret):
    encoded_jwt = jwt.encode(data, secret, algorithm='HS256')
    return encoded_jwt


def verify_signature(token):
    try:
        decoded_jwt = jwt.decode(token, 'acelera', algorithms=['HS256'])
    except jwt.exceptions.InvalidSignatureError:
        return {"error": 2}
    else:  # Executado se não ocorrer erro
        return decoded_jwt
