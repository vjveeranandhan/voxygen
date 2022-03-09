from models import db

class Question_attempt_hdr(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    date=db.Column(db.DateTime)

    # def __init__(self,id, date):
    #         self.id=id
    #         self.date=date

    def from_dict(self, data):
        fields=['date']
        for field in fields:
            setattr(self, field, data[field])
            # data[field]=None if data[field]=="" else data[field]

    def to_dict(self):
        data={
            'id' : self.id,
            'data' : self.date
        }
        return data

    def to_dictionary(self):
        data={
            'date':self.date
        }
        return data
    