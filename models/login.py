import imp
from models import db

class Login(db.Model):
    id=db.Column(db.Integer, priamay_key=True, autoincrement=True)
    username=db.Column(db.Text(120))
    password=db.Column(db.Text(120))

    def from_dict(self, data):
        for field in ['username', 'password']:
            if field in data:
                data[field]=None if data[field]=="" else data[field]

    def to_dict(self):
        data={
            'id': self.id,
            'username': self.username,
            'password': self.password,
        }
        return data