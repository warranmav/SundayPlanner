from app.models import User, db
from werkzeug.security import generate_password_hash

def create_test_user(client):
    user = User(username='testuser', email='test@example.com', password=generate_password_hash('password', method='pbkdf2:sha256'))
    db.session.add(user)
    db.session.commit()
    client.post('/login', data={'email': 'test@example.com', 'password': 'password'})
