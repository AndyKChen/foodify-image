from sqlalchemy import and_
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.mutable import MutableList

from foodify.extensions import db


class ImageModel(db.Model):
    __tablename__ = "Images"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    identifier = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    private = db.Column(db.Boolean, nullable=False)

    def __init__(self,
                 username,
                 identifier,
                 date,
                 private):
        self.username = username
        self.identifier = identifier
        self.date = date
        self.private = private
    
    def json(self):
        json_response = {
            'id': self.id,
            'username': self.username,
            'identifier': self.identifier,
            'date': self.date,
            'private': self.private
        }
        return json_response

    @classmethod
    def get_all_public_images(cls, page_num: int):
        return cls.query.filter(cls.private == False).order_by(cls.date.desc()).paginate(per_page = 10,
                                                                                         page=page_num,
                                                                                         error_out=False)

    @classmethod
    def get_all_images_by_username(cls, username: str):
        return cls.query.filter(cls.username == username).order_by(cls.date.desc()).all()

    @classmethod
    def get_private_images_by_username(cls, username: str, page_num: int):
        return cls.query.filter(and_(cls.username == username),
                                    (cls.private == True)).order_by(cls.date.desc()).paginate(per_page=5,
                                                                                              page=page_num,
                                                                                              error_out=False)
    
    @classmethod
    def get_public_images_by_username(cls, username: str, page_num: int):
        return cls.query.filter(and_(cls.username == username),
                                    (cls.private == False)).order_by(cls.date.desc()).paginate(per_page=5,
                                                                                               page=page_num,
                                                                                               error_out=False)
    
    @classmethod
    def get_image_by_identifier(cls, identifier: str):
        return cls.query.filter(cls.identifier == identifier).first()
    
    def save_to_database(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()
    
    def change_privacy(self):
        self.private = False if self.private else True
        db.session.add(self)
        db.session.commit()