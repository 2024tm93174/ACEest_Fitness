from models import User, db

def test_create_user(app):
    """Ensure user is created in DB"""
    with app.app_context():
        user = User(username="testuser", email="test@example.com")
        db.session.add(user)
        db.session.commit()

        fetched = User.query.filter_by(username="testuser").first()
        assert fetched is not None
        assert fetched.email == "test@example.com"
