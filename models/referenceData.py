from dataclasses import fields
from models import db

class ReferenceData(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    code=db.Column(db.Text(128))
    value=db.Column(db.Text(128))

    def from_dict(self, data):
        for field in ['code', 'value']:
                setattr(self, field, data[field])
                # data[field]=None if data[field]==""  else data[field] 

    def to_dict(self):
        data={
            'id' : self.id,
            'code' : self.code,
            'value' : self.value
        }
        return data