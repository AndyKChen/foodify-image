from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.mutable import MutableList

from shopify_challenge.extensions import db


class ImageModel(db.Model):
    __table__name = "Images"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), db.ForeignKey('Users.username'))
    url = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    labels = db.Column(MutableList.as_mutable(ARRAY(db.String)))
    private = db.Column(db.Boolean, nullable=False)

    def __init__(self,
                 username,
                 url,
                 date,
                 labels,
                 private):
        self.username = username
        self.url = url
        self.date = date
        self.labels = labels
        self.private = private
    
    def json(self):
        json_response = {
            'id': self.id,
            'username': self.username,
            'url': self.url,
            'date': self.date,
            'labels': self.labels,
            'private': self.private
        }
        return json_response

    @classmethod
    def get_all_images(cls):
        return cls.query.all().order_by(cls.date.desc())
    
    def save_to_database(self):
        db.session.add(self)
        db.session.commit()