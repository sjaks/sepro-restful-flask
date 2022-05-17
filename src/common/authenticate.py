from flask_httpauth import HTTPBasicAuth
from models.user import User
import passlib

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and passlib.hash.sha256_crypt.verify(password, user.password_hash):
        return user
