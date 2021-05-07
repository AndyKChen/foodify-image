from shopify_challenge.extensions import db


class UserModel(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    images = db.relationship("ImageModel")

    def __init__(self,
                 first_name,
                 last_name,
                 username,
                 password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def json(self):
        json_response = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'password': self.password
        }
        return json_response
    
    @classmethod
    def find_by_username(cls, username: str):
        return cls.query.filter(cls.username == username).first()

    def save_to_database(self):
        db.session.add(self)
        db.session.commit()
